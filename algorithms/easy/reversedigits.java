// https://leetcode.com/problems/reverse-integer/

class Solution {
    public int reverse(int x) {
        int reversed = 0;
        int digit = 0;
        while (x != 0) {
            digit = x % 10;
            x /= 10;
            // Check for bounds here
            if (reversed > Integer.MAX_VALUE/10 ||
               (reversed == Integer.MAX_VALUE/10 && digit > 7))
                return 0;
            if (reversed < Integer.MIN_VALUE/10 ||
               (reversed == Integer.MIN_VALUE/10 && digit < -8))
                return 0;
            reversed = reversed * 10 + digit;
        }

        return reversed;
    }
}