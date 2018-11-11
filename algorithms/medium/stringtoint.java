// https://leetcode.com/problems/string-to-integer-atoi/

class Solution {
    public int myAtoi(String str) {
        int ret = 0;
        int sign = 1;
        boolean firstCharFound = false;
        boolean signFound = false;
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (!firstCharFound && c == ' ')
                continue;
            if (!firstCharFound && !signFound && (c == '-' || c == '+')) {
                signFound = true;
                sign = (c == '-') ? -1 : 1;
                firstCharFound = true;
                continue;
            }
            firstCharFound = true;
            if (c < '0' || c > '9')
                break;
            int n = c - '0';
            // Overflow check
            if (sign == 1 && (ret > Integer.MAX_VALUE/10 || (ret == Integer.MAX_VALUE/10 && n > 7))) {
                return Integer.MAX_VALUE;
            }
            if (sign < 0 && (-ret < Integer.MIN_VALUE/10 || (-ret == Integer.MIN_VALUE/10 && -n < -8)))
                return Integer.MIN_VALUE;
            ret = ret*10 + n;
        }
        return ret * sign;
    }
}