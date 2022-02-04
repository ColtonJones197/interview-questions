# https://leetcode.com/problems/path-sum/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def isPathSum(root, targetSum):
            newSum = targetSum - root.val
            if newSum == 0 and root.left == None and root.right == None:
                return True
            is_sum = False
            if root.right != None:
                is_sum |= isPathSum(root.right, newSum)
            if root.left != None:
                is_sum |= isPathSum(root.left, newSum)
            return is_sum
        
        if root == None: return False
        return isPathSum(root, targetSum)