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
- Use Binary Search over the range [0, x].
- Repeatedly compute the midpoint.
- If mid² is greater than x, search the left half.
- Otherwise, search the right half.
- Stop when the search interval is within a precision of 1.
- Return the floor of the midpoint of the remaining interval.

Time Complexity: O(log n)
Space Complexity: O(1)

where:
n = x
"""

from math import floor


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            raise ValueError("Negative number.")

        if x == 0 or x == 1:
            return x

        left = 0
        right = max(1, x)
        precision = 1

        while right - left > precision:
            mid = (left + right) / 2

            if mid * mid > x:
                right = mid
            else:
                left = mid

        return floor((left + right) / 2)


if __name__ == "__main__":
    solution = Solution()

    print(solution.mySqrt(4))    # 2
    print(solution.mySqrt(8))    # 2
    print(solution.mySqrt(16))   # 4
    print(solution.mySqrt(25))   # 5
    print(solution.mySqrt(50))   # 7
