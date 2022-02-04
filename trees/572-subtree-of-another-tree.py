# https://leetcode.com/problems/subtree-of-another-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def getSubtree(root, sub) -> bool:
            if root == None:
                return False
            if root.left != None and sub.left == None:
                return False
            if root.right != None and sub.right == None:
                return False
            if root.val != sub.val:
                return False
            left = True
            right = True
            if sub.left != None:
                left = getSubtree(root.left, sub.left)
            if sub.right != None:
                right = getSubtree(root.right, sub.right)
            return right and left
            
        if root == None:
            return subRoot == None
        queue = [root]
        while len(queue) != 0:
            temp = []
            while len(queue) != 0:
                node = queue.pop(0)
                if node.val == subRoot.val:
                    if getSubtree(node, subRoot) == True:
                        return True
                if node.left != None:
                    temp.append(node.left)
                if node.right != None:
                    temp.append(node.right)
            queue = temp
        return False
        