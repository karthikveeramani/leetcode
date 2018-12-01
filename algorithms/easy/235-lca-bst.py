# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
Iterate starting with root node, check if p and q are on either side of tree. If so, root is the LCA.
If root happens to be one of p or q, root is the the LCA (the problem guarantees both values will be in the tree,
so it doesn't matter which side of the tree the other value is)
If both p and q are on left/right side, move root to left/right respectively and repeat until root is null
'''


# Runtime: O(logn), Space: O(1)
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if p == root or q == root: return root
            if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
                return root
            if p.val < root.val and q.val < root.val:
                root = root.left
            else:
                root = root.right
        return None
