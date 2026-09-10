"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # create a hash map of the nodes:
        if node is None:
            return None

        self.clone = {}
        self.cloneNodes(node)
        return self.clone[node]
    

    def cloneNodes(self, node):
        if node not in self.clone:
            copy_node = Node(node.val)
            self.clone[node] = copy_node
            for nei_node in node.neighbors:
                nei_copy_node = self.cloneNodes(nei_node)
                copy_node.neighbors.append(nei_copy_node)
        
        return self.clone[node]

