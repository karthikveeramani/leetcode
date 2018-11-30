# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution(object):
    # Runtime O(n), Space: O(1)
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Assume index1 is at the start, index2 is at the end
        # Now keep adding numbers at index1 and index2 and see if we hit target.             # If not, depending on whether we overshoot the target or are below it,
        # either decrease index2 or increase index1 respectively
        index1 = 0
        index2 = len(numbers) - 1
        while index1 < index2:
            total = numbers[index1] + numbers[index2]
            if total == target:
                return [index1+1,index2+1]
            if total < target:
                index1 = index1 + 1
            elif total > target:
                index2 = index2 - 1

        # If we're here we never found the right combination
        return None
