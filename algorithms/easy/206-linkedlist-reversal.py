# https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime: O(n), Space: O(1)
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverseIterative(head)

    def reverseIterative(self, head):
        if head is None:
            return None
        newhead = head
        head = head.next
        newhead.next = None
        while head:
            tmp = head
            head = head.next
            tmp.next = newhead
            newhead = tmp
        return newhead
