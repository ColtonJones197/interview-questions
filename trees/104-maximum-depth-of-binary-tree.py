# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getMaxDepth(root, prev_depth) -> int:
            current_depth = prev_depth + 1
            left_depth = -1
            right_depth = -1
            if root.left != None:
                left_depth = getMaxDepth(root.left, current_depth)
            if root.right != None:
                right_depth = getMaxDepth(root.right, current_depth)
            return max(current_depth, left_depth, right_depth)
                
        if root == None: return 0
        return getMaxDepth(root, 0)