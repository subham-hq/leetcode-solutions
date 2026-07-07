"""
LeetCode #26 - Remove Duplicates from Sorted Array
Difficulty: Easy

Problem:
Given a sorted integer array nums, remove the duplicates in-place such that
each unique element appears only once.

The relative order of the elements must be preserved.

Return the number of unique elements, k.

The first k elements of nums should contain the unique values in sorted order.
The remaining elements beyond k can be ignored.

Examples:
Input: nums = [1, 1, 2]
Output: 2
nums = [1, 2, _]

Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 5
nums = [0, 1, 2, 3, 4, _, _, _, _, _]

Approach:
- Keep track of the previous unique element.
- Traverse the array once.
- Whenever a new unique value is found, place it at index k and increment k.
- Since the array is sorted, duplicates always appear consecutively.

Time Complexity: O(n)
Space Complexity: O(1)

where:
n = length of the input array
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        prev = None

        for num in nums:
            if prev is None:
                prev = num
                continue

            if num != prev:
                nums[k] = num
                k += 1

            prev = num

        return k


if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 1, 2]
    k1 = solution.removeDuplicates(nums1)
    print(k1)          # 2
    print(nums1[:k1])  # [1, 2]

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = solution.removeDuplicates(nums2)
    print(k2)          # 5
    print(nums2[:k2])  # [0, 1, 2, 3, 4]
