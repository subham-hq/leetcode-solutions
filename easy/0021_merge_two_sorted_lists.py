"""
LeetCode #21 - Merge Two Sorted Lists
Difficulty: Easy

Problem:
You are given the heads of two sorted linked lists, list1 and list2.

Merge the two lists into one sorted linked list. The merged list should be
made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Examples:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]

Approach:
- Create a dummy node to simplify edge cases.
- Use a pointer (current) to build the merged list.
- Compare the current nodes of both lists.
- Attach the smaller node to the merged list and move that list's pointer.
- Once one list is exhausted, attach the remaining nodes of the other list.
- Return the node after the dummy node.

Time Complexity: O(n + m)
Space Complexity: O(1)

where:
n = number of nodes in list1
m = number of nodes in list2
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next
