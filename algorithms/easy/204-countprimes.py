# https://leetcode.com/problems/count-primes/

import math

# Runtime: O(n2)?, Space: O(1)
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in xrange(2,n):
            if self.isPrime(i):
                count = count + 1
        return count

    def isPrime(self, n):
        if n <= 1: return False
        if n <= 3: return True
        if n%2 == 0 or n%3 == 0: return False
        for i in xrange(5,int(math.sqrt(n))+1,6):
            if n%i == 0 or n%(i+2) == 0: return False
        return True