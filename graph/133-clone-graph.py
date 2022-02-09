# https://leetcode.com/problems/clone-graph/
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        def clone(node: 'Node'):
            if node in visited:
                return visited[node]
            new_node = Node(node.val)
            visited[node] = new_node
            for adj in node.neighbors:
                new_node.neighbors.append(clone(adj))
            return new_node
        
        return clone(node) if node else None