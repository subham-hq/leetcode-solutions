"""
LeetCode #70 - Climbing Stairs
Difficulty: Easy

Problem:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.

Return the number of distinct ways to climb to the top.

Examples:
Input: n = 2
Output: 2

Input: n = 3
Output: 3

Approach:
- Use recursion with memoization (Top-Down Dynamic Programming).
- The number of ways to reach step n is the sum of:
    - the ways to reach step n - 1
    - the ways to reach step n - 2
- Store previously computed results to avoid redundant calculations.

Time Complexity: O(n)
Space Complexity: O(n)

where:
n = number of steps
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(n: int) -> int:
            if n == 1:
                return 1

            if n == 2:
                return 2

            if n in memo:
                return memo[n]

            memo[n] = climb(n - 1) + climb(n - 2)

            return memo[n]

        return climb(n)


if __name__ == "__main__":
    solution = Solution()

    print(solution.climbStairs(1))  # 1
    print(solution.climbStairs(2))  # 2
    print(solution.climbStairs(3))  # 3
    print(solution.climbStairs(4))  # 5
    print(solution.climbStairs(5))  # 8
