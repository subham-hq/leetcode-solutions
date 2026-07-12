"""
LeetCode #66 - Plus One
Difficulty: Easy

Problem:
You are given a large integer represented as an array of digits, where each
digit represents a single decimal digit.

Increment the integer by one and return the resulting array of digits.

Examples:
Input: digits = [1, 2, 3]
Output: [1, 2, 4]

Input: digits = [4, 3, 2, 1]
Output: [4, 3, 2, 2]

Input: digits = [9]
Output: [1, 0]

Approach:
- Start from the least significant digit.
- Add one to the last digit.
- Propagate any carry towards the most significant digit.
- If a carry remains after processing all digits, prepend 1.

Time Complexity: O(n)
Space Complexity: O(1)

where:
n = number of digits
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 0

        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                digits[i] += 1

            digits[i] += carry

            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            else:
                carry = 0

        if carry:
            digits = [1] + digits

        return digits


if __name__ == "__main__":
    solution = Solution()

    print(solution.plusOne([1, 2, 3]))       # [1, 2, 4]
    print(solution.plusOne([4, 3, 2, 1]))    # [4, 3, 2, 2]
    print(solution.plusOne([9]))             # [1, 0]
    print(solution.plusOne([9, 9, 9]))       # [1, 0, 0, 0]
