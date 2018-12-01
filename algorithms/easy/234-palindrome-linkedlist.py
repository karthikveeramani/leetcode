# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime: O(n), Space: O(1)
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Idea: reverse first half of the list (not taking up extra space)
        # then compare the reversed first half with original second half
        # O(n) to get list length, O(n/2) to reverse first half, O(n/2) to
        # compare two halves. If list needs to stay unmodified, you can reverse
        # the first half again and stick it to the 2nd, which will be O(n/2)
        # Total is O(2n) without the last step, which is O(n)

        n = self._len(head)
        if n <= 1:
            return True
        firsthalfrev,sechalf = self._reverse(head, int(n/2))
        # If n is odd, we need to account for the middle number
        if n%2 != 0:
            sechalf = sechalf.next
        while sechalf:
            if firsthalfrev.val != sechalf.val: return False
            sechalf = sechalf.next
            firsthalfrev = firsthalfrev.next
        return True

    def _reverse(self, head, n):
        newhead = None
        for i in xrange(0,n):
            if newhead is None:
                newhead = head
                head = head.next
                newhead.next = None
            else:
                tmp = head
                head = head.next
                tmp.next = newhead
                newhead = tmp
        return newhead,head

    def _len(self, head):
        count = 0
        while (head):
            count = count + 1
            head = head.next
        return count