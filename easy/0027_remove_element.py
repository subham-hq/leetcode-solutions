"""
LeetCode #27 - Remove Element
Difficulty: Easy

Problem:
Given an integer array nums and an integer val, remove all occurrences of
val in-place.

The relative order of the remaining elements may be changed.

Return the number of elements in nums that are not equal to val.

The first k elements of nums should contain all elements not equal to val.
The remaining elements beyond k can be ignored.

Examples:
Input: nums = [3, 2, 2, 3], val = 3
Output: 2
nums = [2, 2, _, _]

Input: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
Output: 5
nums = [0, 1, 4, 0, 3, _, _, _]

Approach:
- Maintain an index k representing the position where the next valid
  element should be placed.
- Traverse the array once.
- If the current element is not equal to val, place it at index k and
  increment k.
- After traversal, the first k elements contain all remaining values.

Time Complexity: O(n)
Space Complexity: O(1)

where:
n = length of the input array
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k


if __name__ == "__main__":
    solution = Solution()

    nums1 = [3, 2, 2, 3]
    k1 = solution.removeElement(nums1, 3)
    print(k1)          # 2
    print(nums1[:k1])  # [2, 2]

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    k2 = solution.removeElement(nums2, 2)
    print(k2)          # 5
    print(nums2[:k2])  # [0, 1, 3, 0, 4]
