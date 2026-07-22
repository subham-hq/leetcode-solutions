"""
LeetCode #88 - Merge Sorted Array
Difficulty: Easy

Problem:
You are given two integer arrays, nums1 and nums2, sorted in non-decreasing
order, along with two integers m and n representing the number of valid
elements in each array.

Merge nums2 into nums1 as one sorted array in-place.

Examples:
Input:
nums1 = [1, 2, 3, 0, 0, 0], m = 3
nums2 = [2, 5, 6], n = 3

Output:
[1, 2, 2, 3, 5, 6]

Input:
nums1 = [1], m = 1
nums2 = [], n = 0

Output:
[1]

Input:
nums1 = [0], m = 0
nums2 = [1], n = 1

Output:
[1]

Approach:
- Use three pointers:
    - i points to the last valid element in nums1.
    - j points to the last element in nums2.
    - k points to the last position in nums1.
- Compare nums1[i] and nums2[j].
- Place the larger value at nums1[k].
- Continue until one array is exhausted.
- If elements remain in nums2, copy them into nums1.

Time Complexity: O(m + n)
Space Complexity: O(1)

where:
m = number of valid elements in nums1
n = number of elements in nums2
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    solution.merge(nums1, 3, [2, 5, 6], 3)
    print(nums1)  # [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    solution.merge(nums1, 1, [], 0)
    print(nums1)  # [1]

    nums1 = [0]
    solution.merge(nums1, 0, [1], 1)
    print(nums1)  # [1]
