"""
LeetCode #58 - Length of Last Word
Difficulty: Easy

Problem:
Given a string s consisting of words and spaces, return the length of the
last word in the string.

A word is defined as a maximal substring consisting of non-space characters.

Examples:
Input: s = "Hello World"
Output: 5

Input: s = "   fly me   to   the moon  "
Output: 4

Input: s = "luffy is still joyboy"
Output: 6

Approach:
- Split the string into words using whitespace as the delimiter.
- Access the last word in the resulting list.
- Return its length.

Time Complexity: O(n)
Space Complexity: O(n)

where:
n = length of the input string
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])


if __name__ == "__main__":
    solution = Solution()

    print(solution.lengthOfLastWord("Hello World"))                 # 5
    print(solution.lengthOfLastWord("   fly me   to   the moon  ")) # 4
    print(solution.lengthOfLastWord("luffy is still joyboy"))       # 6
