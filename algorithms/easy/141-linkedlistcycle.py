# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime: O(n), Space: O(1)
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        fast = head
        slow = head
        while fast.next is not None:
            fast = fast.next
            if fast.next is None:
                return False
            fast = fast.next
            if fast == slow:
                return True
            slow = slow.next
        return False
