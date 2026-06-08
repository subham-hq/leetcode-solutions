"""
LeetCode #1 - Two Sum
Difficulty: Easy

Problem:
Given an array of integers nums and an integer target, return the indices
of the two numbers such that they add up to target.

You may assume that each input has exactly one solution, and you may not
use the same element twice.

Examples:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]

Input: nums = [3, 2, 4], target = 6
Output: [1, 2]

Input: nums = [3, 3], target = 6
Output: [0, 1]

Approach:
- Use a hash map (dictionary) to store previously seen numbers and their indices.
- For each number, calculate the complement needed to reach the target.
- If the complement already exists in the hash map, return the indices.
- Otherwise, store the current number and its index.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], index]

            seen[num] = index


if __name__ == "__main__":
    solution = Solution()

    print(solution.twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(solution.twoSum([3, 2, 4], 6))       # [1, 2]
    print(solution.twoSum([3, 3], 6))          # [0, 1]
