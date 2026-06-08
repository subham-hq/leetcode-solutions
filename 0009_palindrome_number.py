"""
LeetCode #9 - Palindrome Number
Difficulty: Easy

Problem:
Given an integer x, return True if x is a palindrome, and False otherwise.

A palindrome number reads the same forward and backward.

Examples:
Input: x = 121
Output: True

Input: x = -121
Output: False

Input: x = 10
Output: False

Approach:
- Negative numbers cannot be palindromes because of the '-' sign.
- Convert the integer to a string.
- Compare the string with its reversed version.
- If both are equal, the number is a palindrome.

Time Complexity: O(n)
Space Complexity: O(n)
where n is the number of digits in the integer.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num_str = str(x)
        return num_str == num_str[::-1]


if __name__ == "__main__":
    solution = Solution()

    print(solution.isPalindrome(121))    # True
    print(solution.isPalindrome(-121))   # False
    print(solution.isPalindrome(10))     # False
    print(solution.isPalindrome(12321))  # True
