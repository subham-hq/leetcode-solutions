"""
LeetCode #28 - Find the Index of the First Occurrence in a String
Difficulty: Easy

Problem:
Given two strings, needle and haystack, return the index of the first
occurrence of needle in haystack.

If needle is not part of haystack, return -1.

Examples:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Input: haystack = "leetcode", needle = "leeto"
Output: -1

Approach:
- Use Python's built-in string method `find()`.
- `find()` returns the index of the first occurrence of the substring.
- If the substring is not found, it returns -1.

Time Complexity: O(n * m) in the worst case
Space Complexity: O(1)

where:
n = length of haystack
m = length of needle
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == "__main__":
    solution = Solution()

    print(solution.strStr("sadbutsad", "sad"))   # 0
    print(solution.strStr("leetcode", "leeto"))  # -1
    print(solution.strStr("hello", "ll"))        # 2
    print(solution.strStr("aaaaa", "bba"))       # -1
