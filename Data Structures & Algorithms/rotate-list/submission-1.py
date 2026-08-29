# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        # Traverse to find the length of the linkedlist
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        
        k = k % n
        if k == 0:
            return head

        dummy = ListNode()
        p1 = head

        node = head
        for _ in range(n-k-1):
            node = node.next
        
        p2 = node.next
        node.next = None

        dummy.next = p2

        node = p2
        for _ in range(k-1):
            node = node.next
        
        node.next = p1
        return dummy.next
