// https://leetcode.com/problems/binary-tree-pruning/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    // Runtime: O(logN), Space: O(N)?
    public TreeNode pruneTree(TreeNode root) {
        if (gotOne(root)) return root;
        return null;
    }

    private boolean gotOne(TreeNode node) {
        if (node == null)
            return false;
        boolean leftHasOne = gotOne(node.left);
        boolean rightHasOne = gotOne(node.right);
        if (!leftHasOne)
            node.left = null;
        if (!rightHasOne)
            node.right = null;
        boolean iHaveOne = node.val == 1;
        if (!iHaveOne && !leftHasOne && !rightHasOne)
            return false; // chop this node
        return true;
    }
}