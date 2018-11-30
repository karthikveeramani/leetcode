# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def _len(self, head):
        n = 0
        while head:
            head = head.next
            n = n + 1
        return n

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Solution 1: O(n + m) runtime and O(n) space where n = len(headA)
        # Iterate through headA and add nodes to a set
        # Iterate through headB and check if each node is in the set
        # If present, that's the first intersection point
        # If iteration ends, no intersection

        # Solution 2: Runtime O(2(n+m)), space O(1)
        # n = len(headA) m = len(headB)
        # Push by abs(n-m) nodes the list that's max(n,m)
        # Move one node per list and compare for equality
        # If any list ends on the way, no intersection
        if headA is None or headB is None:
            return None
        n = self._len(headA)
        m = self._len(headB)
        diff = abs(n-m)
        if n > m:
            longer = headA
            other = headB
        else:
            longer = headB
            other = headA
        if diff > 0:
            for i in xrange(0,diff):
                longer = longer.next
        while longer and other:
            if longer == other:
                return longer
            longer = longer.next
            other = other.next
        return None
