# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None

        dummy = ListNode()
        dummy.next = head

        curr = head
        prev = dummy

        while curr:
            nxt = curr.next
            if curr.val == val:
                curr.next = None
                prev.next = nxt
            else:
                prev = curr
            
            curr = nxt
        
        return dummy.next


