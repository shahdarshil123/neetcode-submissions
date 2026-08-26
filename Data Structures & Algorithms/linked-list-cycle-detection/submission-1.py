# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = set()
        node = head

        if node is None:
            return False

        while node:
            if node in node_set:
                return True
            node_set.add(node)
            node = node.next
        
        return False