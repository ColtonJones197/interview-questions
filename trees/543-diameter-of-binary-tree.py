# https://leetcode.com/problems/diameter-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getLongestLength(root, pathLength, lengths):
            #if it's a leaf, return 0
            if root.left == None and root.right == None:
                return 0
            left_length = 0
            right_length = 0
            if root.left != None:
                left_length = 1 + getLongestLength(root.left, pathLength + 1, lengths)
            if root.right != None:
                right_length = 1 + getLongestLength(root.right, pathLength + 1, lengths)
            max_length_at_node = left_length + right_length
            lengths.append(max_length_at_node)
            return max(left_length, right_length)
            
        lengths = []
        num = getLongestLength(root, 0, lengths)
        if num == 0:
            return 0
        lengths.sort()
        return lengths[-1]
                