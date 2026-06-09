#!/usr/bin/env python3
"""
Auto-update the LeetCode-solutions README.

Scans the easy/, medium/ and hard/ folders for solution files named like
`0001_two_sum.py` and regenerates three marker-delimited regions in README.md:

    <!-- STATS:START -->      progress table (counts per difficulty)   <!-- STATS:END -->
    <!-- TREE:START -->       directory tree of all solutions          <!-- TREE:END -->
    <!-- SOLUTIONS:START -->  per-difficulty index tables with links   <!-- SOLUTIONS:END -->

Any region whose markers are missing is simply skipped, so you can delete a
section from the README (e.g. drop the tree once it gets long) without touching
this script.

File-naming convention (keep to this and the links stay correct):

    <number>_<leetcode-slug-with-underscores>.py
    e.g.  0001_two_sum.py  ->  #1  "Two Sum"  https://leetcode.com/problems/two-sum/

Run from the repository root:
    python scripts/update_readme.py
"""

from __future__ import annotations

import re
from pathlib import Path

# ---- Configuration ---------------------------------------------------------

README = Path("README.md")
DIFFICULTIES = ["easy", "medium", "hard"]          # these are also the folder names
SOLUTION_RE = re.compile(r"^(\d+)_(.+)\.py$")      # matches 0001_two_sum.py
LEETCODE_BASE = "https://leetcode.com/problems"
EMOJI = {"easy": "\U0001F7E2", "medium": "\U0001F7E1", "hard": "\U0001F534"}  # 🟢 🟡 🔴

# Tokens that should render fully uppercase in a displayed title.
ACRONYMS = {"ii", "iii", "iv", "vi", "vii", "lru", "lfu", "bst", "api", "sql", "url", "tv", "rgb"}

# ---- Helpers ---------------------------------------------------------------


def title_from_slug(slug: str) -> str:
    """two_sum -> 'Two Sum'  (best-effort; edit by hand for odd casing)."""
    out = []
    for word in slug.split("_"):
        if word.lower() in ACRONYMS:
            out.append(word.upper())
        elif word.isdigit():
            out.append(word)
        else:
            out.append(word.capitalize())
    return " ".join(out)


def url_from_slug(slug: str) -> str:
    """two_sum -> https://leetcode.com/problems/two-sum/"""
    return f"{LEETCODE_BASE}/{slug.replace('_', '-')}/"


def collect() -> dict[str, list[tuple[int, str, str]]]:
    """Return {difficulty: [(number, slug, filename), ...]} sorted by number."""
    data: dict[str, list[tuple[int, str, str]]] = {d: [] for d in DIFFICULTIES}
    for difficulty in DIFFICULTIES:
        folder = Path(difficulty)
        if not folder.is_dir():
            continue
        for entry in folder.iterdir():
            if not entry.is_file():
                continue
            match = SOLUTION_RE.match(entry.name)
            if not match:
                continue
            data[difficulty].append((int(match.group(1)), match.group(2), entry.name))
        data[difficulty].sort(key=lambda item: item[0])
    return data


# ---- Section builders ------------------------------------------------------


def build_stats(data) -> str:
    counts = {d: len(v) for d, v in data.items()}
    total = sum(counts.values())
    return "\n".join(
        [
            "| Difficulty | Solved |",
            "|:-----------|-------:|",
            f"| {EMOJI['easy']} Easy | {counts['easy']} |",
            f"| {EMOJI['medium']} Medium | {counts['medium']} |",
            f"| {EMOJI['hard']} Hard | {counts['hard']} |",
            f"| **Total** | **{total}** |",
        ]
    )


def build_tree(data) -> str:
    lines = ["```text", "leetcode-solutions/"]
    for difficulty in DIFFICULTIES:
        lines.append(f"\u251c\u2500\u2500 {difficulty}/")          # ├──
        files = data[difficulty]
        for index, (_, _, filename) in enumerate(files):
            branch = "\u2514\u2500\u2500" if index == len(files) - 1 else "\u251c\u2500\u2500"
            lines.append(f"\u2502   {branch} {filename}")          # │   ├── / └──
    lines.append("\u2514\u2500\u2500 README.md")                   # └── README.md
    lines.append("```")
    return "\n".join(lines)


def build_solutions(data) -> str:
    blocks = []
    for difficulty in DIFFICULTIES:
        files = data[difficulty]
        header = f"### {EMOJI[difficulty]} {difficulty.capitalize()} ({len(files)})"
        if not files:
            blocks.append(f"{header}\n\n_No solutions yet._")
            continue
        rows = ["| # | Problem | Solution |", "|--:|:--------|:---------|"]
        for number, slug, filename in files:
            rows.append(
                f"| {number} "
                f"| [{title_from_slug(slug)}]({url_from_slug(slug)}) "
                f"| [Python](./{difficulty}/{filename}) |"
            )
        blocks.append(f"{header}\n\n" + "\n".join(rows))
    return "\n\n".join(blocks)


# ---- Marker replacement ----------------------------------------------------


def replace_region(text: str, name: str, payload: str) -> str:
    start, end = f"<!-- {name}:START -->", f"<!-- {name}:END -->"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    if not pattern.search(text):
        print(f"  - {name}: markers not found, skipping")
        return text
    print(f"  - {name}: updated")
    return pattern.sub(lambda _match: f"{start}\n{payload}\n{end}", text)


def main() -> None:
    if not README.exists():
        raise SystemExit("README.md not found. Run this from the repository root.")
    data = collect()
    text = README.read_text(encoding="utf-8")
    print("Regenerating README sections:")
    text = replace_region(text, "STATS", build_stats(data))
    text = replace_region(text, "TREE", build_tree(data))
    text = replace_region(text, "SOLUTIONS", build_solutions(data))
    README.write_text(text, encoding="utf-8")
    counts = {d: len(v) for d, v in data.items()}
    print(
        f"Done. easy={counts['easy']} medium={counts['medium']} "
        f"hard={counts['hard']} total={sum(counts.values())}"
    )


if __name__ == "__main__":
    main()
