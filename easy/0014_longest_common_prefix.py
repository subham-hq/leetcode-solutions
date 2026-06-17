"""
LeetCode #14 - Longest Common Prefix
Difficulty: Easy

Problem:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Examples:
Input: strs = ["flower", "flow", "flight"]
Output: "fl"

Input: strs = ["dog", "racecar", "car"]
Output: ""

Approach:
- Assume the first string is the common prefix.
- Compare it with every other string.
- Count matching characters from the beginning.
- Trim the prefix to the matched portion.
- If the prefix becomes empty, return immediately.

Time Complexity: O(n * m)
Space Complexity: O(1)

where:
n = number of strings
m = length of the shortest common prefix
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        result = strs[0]

        for word in strs[1:]:
            match_count = 0

            for ch1, ch2 in zip(word, result):
                if ch1 == ch2:
                    match_count += 1
                else:
                    break

            result = result[:match_count]

            if not result:
                return ""

        return result


if __name__ == "__main__":
    solution = Solution()

    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # fl
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))     # ""
    print(solution.longestCommonPrefix(["apple", "app", "application"]))  # app
