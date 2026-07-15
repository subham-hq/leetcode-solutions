"""
LeetCode #69 - Sqrt(x)
Difficulty: Easy

Problem:
Given a non-negative integer x, return the square root of x rounded down to
the nearest integer.

The returned integer should be non-negative.

Do not use any built-in exponent function or operator.

Examples:
Input: x = 4
Output: 2

Input: x = 8
Output: 2

Approach:
- Use Binary Search to find the integer square root.
- Search within the range [1, x // 2 + 1].
- If mid² equals x, return mid.
- If mid² is less than x, continue searching the right half.
- Otherwise, search the left half.
- If the exact square root is not found, return the largest integer whose
  square is less than x.

Time Complexity: O(log n)
Space Complexity: O(1)

where:
n = x
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 1
        right = x // 2 + 1

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                left = mid + 1

            else:
                right = mid - 1

        return right


if __name__ == "__main__":
    solution = Solution()

    print(solution.mySqrt(0))    # 0
    print(solution.mySqrt(1))    # 1
    print(solution.mySqrt(4))    # 2
    print(solution.mySqrt(8))    # 2
    print(solution.mySqrt(16))   # 4
    print(solution.mySqrt(50))   # 7
