"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        
        copy_map = {None: None}

        node = head
        while node:
            copy_node = Node(node.val)
            copy_map[node] = copy_node
            node = node.next
        
        node = head
        while node:
            copy_map[node].next = copy_map[node.next]
            copy_map[node].random = copy_map[node.random]
            node = node.next

        return copy_map[head]
