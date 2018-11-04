// https://leetcode.com/problems/add-two-numbers/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode outTop = null;
        ListNode current = outTop;

        while (true) {
            if (l1 == null && l2 == null) break;
            int l1val = 0;
            int l2val = 0;
            if (l1 != null) {
                l1val = l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                l2val = l2.val;
                l2 = l2.next;
            }

            int total = l1val + l2val + carry;
            if (total >= 10) {
                carry = 1;
                total = total - 10;
            }
            else {
                carry = 0;
            }
            ListNode n = new ListNode(total);
            if (current == null) {
                current = n;
                outTop = n;
            }
            else {
                current.next = n;
                current = current.next;
            }
        }
        if (carry == 1) {
            // Insert the last number
            current.next = new ListNode(1);
        }
        return outTop;
    }
}