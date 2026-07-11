"""
LeetCode #35 - Search Insert Position
Difficulty: Easy

Problem:
Given a sorted array of distinct integers and a target value, return the
index if the target is found.

If the target is not found, return the index where it would be inserted to
maintain the sorted order.

Examples:
Input: nums = [1, 3, 5, 6], target = 5
Output: 2

Input: nums = [1, 3, 5, 6], target = 2
Output: 1

Input: nums = [1, 3, 5, 6], target = 7
Output: 4

Approach:
- Traverse the array from left to right.
- If an element greater than or equal to the target is found,
  return its index.
- If the loop finishes, the target belongs at the end of the array.

Time Complexity: O(n)
Space Complexity: O(1)

Note:
The problem requires an O(log n) solution using Binary Search.
This implementation is correct but does not satisfy that runtime requirement.
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        index = 0

        for num in nums:
            if num >= target:
                break
            index += 1

        return index


if __name__ == "__main__":
    solution = Solution()

    print(solution.searchInsert([1, 3, 5, 6], 5))  # 2
    print(solution.searchInsert([1, 3, 5, 6], 2))  # 1
    print(solution.searchInsert([1, 3, 5, 6], 7))  # 4
    print(solution.searchInsert([1, 3, 5, 6], 0))  # 0
