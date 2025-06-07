"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    # O(n)
    def cloneGraph(self, node):
        if not node:
            return None

        hashmap = {}

        def dfs(nodee):
            if nodee in hashmap:
                return hashmap[nodee]

            cp = Node(nodee.val)
            hashmap[nodee] = cp
            for neighbor in nodee.neighbors:
                cp.neighbors.append(dfs(neighbor))
        
            return cp
        
        return dfs(node)