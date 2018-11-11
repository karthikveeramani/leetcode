// https://leetcode.com/problems/valid-parentheses/

class Solution {
    // Runtime: O(n), Space: O(n)
    public boolean isValid(String s) {
        if ("".equals(s))
            return true;
        Deque<Character> q = new ArrayDeque();
        HashMap<Character, Character> map = new HashMap();
        map.put('}', '{');
        map.put(')', '(');
        map.put(']', '[');

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '{' || c == '[' || c == '(') {
                q.addFirst(Character.valueOf(c));
                continue;
            }
            if (c == '}' || c == ']' || c == ')') {
                if (q.isEmpty())
                    return false;
                if (!map.get(Character.valueOf(c)).equals(q.removeFirst()))
                    return false;
            }
        }
        if (!q.isEmpty())
            return false;
        return true;
    }
}
