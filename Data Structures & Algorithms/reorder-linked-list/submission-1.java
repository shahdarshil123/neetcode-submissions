/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;

        //Initialize fast & slow pointers
        ListNode slow = head;
        ListNode fast = head;

        ListNode prev = null;
        ListNode nxt = null;

        //Reverse the linked list
        while(fast != null && fast.next != null){
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        prev.next = null;
        prev = null;

        while(slow != null){
            nxt = slow.next;
            slow.next = prev;
            prev = slow;
            slow = nxt;
        }

        ListNode start = head;
        ListNode end = prev;
        ListNode startNxt = null;
        ListNode endNxt = null;

        // Check if reversed properly
        // while(ptr2 != null){
        //     System.out.println(ptr2.val);
        //     ptr2 = ptr2.next;
        // }

        // Reorder the list now
        head = start;
        while(start != null && end != null){
            startNxt = start.next;
            endNxt = end.next;

            start.next = end;
            if (startNxt == null) break;
            end.next = startNxt;

            start = startNxt;
            end = endNxt;
        }
    }
}