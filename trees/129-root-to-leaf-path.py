# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def rootToLeafPath(node: Optional[TreeNode], result, prev: str) -> None:
            new_prev = prev + str(node.val)
            if node.left is None and node.right is None:
                result.append(new_prev)
            if node.left:
                rootToLeafPath(node.left, result, new_prev)
            if node.right:
                rootToLeafPath(node.right, result, new_prev)
        result = []
        rootToLeafPath(root, result, '')
        rtlpSum = 0
        for entry in result:
            rtlpSum += int(entry)
        return rtlpSum
                