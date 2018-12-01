# https://leetcode.com/problems/reverse-nodes-in-k-group/

'''
Idea: For every k nodes, reverse, stitch to an output list
If remaining < k, don't reverse, just stitch
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def printall(head):
    while head:
        print " {}".format(head.val)
        head = head.next

# Runtime: O(n), Space: O(1)
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n = self._len(head)
        rem = n
        outhead = ListNode(0) # dummy
        outtail = outhead
        while (head):
            if rem >= k:
                reversed,head,complete = self._reverse(head,k)
                rem = rem - k
            else:
                reversed,head,complete = None,head,False
            join_list = reversed if complete else head
            if join_list is None:
                break
            outtail.next = join_list
            while join_list.next:
                join_list = join_list.next
            outtail = join_list
            if not complete:
                break
        return outhead.next

    def _reverse(self, head, n):
        newhead = None
        complete = True
        for i in xrange(0, n):
            if head is None:
                complete = False
                break
            if newhead is None:
                newhead = head
                head = head.next
                newhead.next = None
            else:
                tmp = head
                head = head.next
                tmp.next = newhead
                newhead = tmp
        return newhead,head,complete

    def _len(self, head):
        count = 0
        while head:
            count = count + 1
            head = head.next
        return count