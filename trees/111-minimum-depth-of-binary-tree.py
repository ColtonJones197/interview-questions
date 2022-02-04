# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #if finding minimum depth we probably want another bfs
        if root == None: return 0
        unexplored = [root]
        min_depth = 1
        while len(unexplored) != 0:
            next_level = []
            while(len(unexplored) != 0):
                node = unexplored.pop(0)
                if node.left == None and node.right == None:
                    return min_depth
                if node.left != None:
                    next_level.append(node.left)
                if node.right != None:
                    next_level.append(node.right)
            min_depth += 1
            unexplored = next_level