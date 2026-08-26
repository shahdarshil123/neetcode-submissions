class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # Reach mid of the list by using slow and fast pointers
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the right half of the linked list
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # make left and right pointer on the list
        left = head
        right = prev
        
        while right:
            left_nxt = left.next
            right_nxt = right.next
            
            left.next = right
            right.next = left_nxt
            
            left = left_nxt
            right = right_nxt