# https://leetcode.com/problems/valid-anagram/

'''
Idea: Build a histogram off 1st string and use it to compare the 2nd string
For space efficiency, create an array of all possible chars (a-z) so we get
O(1) lookup and constant space. Populate the slots of this array with no. of
times each char occurs in string s. Then iterate through string t and cross
off the corresponding characters in the previously built histogram.
'''

# Runtime: O(n+m), Space: O(1)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Build histogram with s
        hist = [0 for i in xrange(0, ord('z')-ord('a')+1)]
        a = ord('a')
        for i in s:
            i = ord(i) - a
            hist[i] = hist[i]+1

        # Iterate through t and compare
        for i in t:
            i = ord(i) - a
            if hist[i] <= 0: return False
            hist[i] = hist[i] - 1

        # This is to account for cases with mismatched length of t and s
        return sum(hist) == 0

