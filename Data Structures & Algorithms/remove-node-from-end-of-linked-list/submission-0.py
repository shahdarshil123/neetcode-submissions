# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        dummy = ListNode()
        dummy.next = head
        right = dummy

        while right:
            
            if count == n:
                prev = dummy
                left = head
            
            elif count > n:
                prev = left
                left  = left.next 
            
            right = right.next
            count += 1
        
        nxt = left.next
        left.next = None
        prev.next = nxt

        return dummy.next
