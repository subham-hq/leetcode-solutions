"""
LeetCode #83 - Remove Duplicates from Sorted List
Difficulty: Easy

Problem:
Given the head of a sorted linked list, delete all duplicates such that each
element appears only once.

Return the linked list sorted as well.

Examples:
Input: head = [1, 1, 2]
Output: [1, 2]

Input: head = [1, 1, 2, 3, 3]
Output: [1, 2, 3]

Approach:
- Traverse the sorted linked list using a pointer.
- Compare the current node's value with the next node's value.
- If the values are different, link the unique node to the result.
- Skip duplicate nodes by not updating the result pointer.
- After traversal, terminate the list by setting the last unique node's next
  pointer to None.

Time Complexity: O(n)
Space Complexity: O(1)

where:
n = number of nodes in the linked list
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        curr = head
        output = head

        while curr.next is not None:
            temp = curr.val
            curr = curr.next

            if temp != curr.val:
                output.next = curr
                output = output.next

        output.next = None

        return head
