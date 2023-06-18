"""
61. Rotate List
Medium
8K
1.4K
Companies
Given the head of a linked list, rotate the list to the right by k places.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        if size == 0:
            return head
        k = k % size
        if k == 0:
            return head
        cur = head
        for i in range(size - k - 1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        cur = newHead
        while cur.next:
            cur = cur.next
        cur.next = head
        return newHead
