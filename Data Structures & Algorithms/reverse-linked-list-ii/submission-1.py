# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # D, 1, 2, 3, 4, 5

        if left == right:
            return head

        dummy = ListNode()
        dummy.next = head

        prev = dummy
        curr = dummy.next

        for _ in range(left-1):
            prev = curr
            curr = curr.next
        
        prev.next = None

        p = None
        n = curr
        for _ in range(right-left+1):
            nxt = curr.next
            curr.next = p
            p = curr
            curr = nxt
        
        n.next = curr
        prev.next = p

        return dummy.next
        


