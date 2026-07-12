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
- Traverse the digits from right to left.
- If the current digit is less than 9, increment it and return immediately.
- Otherwise, set the current digit to 0 and continue carrying to the left.
- If all digits were 9, prepend 1 to the array.

Time Complexity: O(n)
Space Complexity: O(1)

where:
n = number of digits
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits


if __name__ == "__main__":
    solution = Solution()

    print(solution.plusOne([1, 2, 3]))       # [1, 2, 4]
    print(solution.plusOne([4, 3, 2, 1]))    # [4, 3, 2, 2]
    print(solution.plusOne([9]))             # [1, 0]
    print(solution.plusOne([9, 9, 9]))       # [1, 0, 0, 0]
