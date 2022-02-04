# https://leetcode.com/problems/merge-two-binary-trees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(root1, root2) -> Optional[TreeNode]:
            if root1 == None:
                return root2
            if root2 == None:
                return root1
            new_val = root1.val + root2.val
            new_left = merge(root1.left, root2.left)
            new_right = merge(root1.right, root2.right)
            new_node = TreeNode(new_val, new_left, new_right)
            return new_node
        return merge(root1, root2)