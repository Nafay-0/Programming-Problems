"""
25. Reverse Nodes in k-Group
Hard
10.5K
562
Companies
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]


Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        temp = head
        for i in range(k):
            if temp is None:
                return head
            temp = temp.next
        new_head = self.reverse(head, temp)
        head.next = self.reverseKGroup(temp, k)
        return new_head

    def reverse(self, head, temp):
        prev = temp
        while head != temp:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
