# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        unexplored = [root]
        averages = []
        #while there are no levels left
        while len(unexplored) != 0:
            total = 0
            count = 0
            nodes_on_next_level = []
            while(len(unexplored) != 0):
                node = unexplored.pop(0)
                total += node.val
                count += 1
                if node.left != None:
                    nodes_on_next_level.append(node.left)
                if node.right != None:
                    nodes_on_next_level.append(node.right)
            #find the average of each value and add it to the list of averages
            averages.append(round(total * 1.0 / count, 5))
            unexplored = nodes_on_next_level
        return averages