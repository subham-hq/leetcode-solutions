"""
LeetCode #35 - Search Insert Position
Difficulty: Easy

Problem:
Given a sorted array of distinct integers and a target value, return the
index if the target is found.

If the target is not found, return the index where it would be inserted to
maintain the sorted order.

You must write an algorithm with O(log n) runtime complexity.

Examples:
Input: nums = [1, 3, 5, 6], target = 5
Output: 2

Input: nums = [1, 3, 5, 6], target = 2
Output: 1

Input: nums = [1, 3, 5, 6], target = 7
Output: 4

Approach:
- Use Binary Search to repeatedly divide the search space in half.
- If the target is found, return its index.
- If the target is not found, the left pointer indicates the correct
  insertion position.

Time Complexity: O(log n)
Space Complexity: O(1)

where:
n = length of the input array
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    solution = Solution()

    print(solution.searchInsert([1, 3, 5, 6], 5))  # 2
    print(solution.searchInsert([1, 3, 5, 6], 2))  # 1
    print(solution.searchInsert([1, 3, 5, 6], 7))  # 4
    print(solution.searchInsert([1, 3, 5, 6], 0))  # 0
