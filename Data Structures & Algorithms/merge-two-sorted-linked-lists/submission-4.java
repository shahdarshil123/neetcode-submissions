/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) {\ this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode node1 = list1;
        ListNode node2 = list2;
        ListNode dummy = new ListNode();
        ListNode node = dummy;

        while(node1 != null && node2 != null){
            if(node1.val <= node2.val){
                node.next = node1;
                node1 = node1.next;
            }
            else{
                node.next = node2;
                node2 = node2.next;
            }
            node = node.next;
        }
        if(node1 != null){
            node.next = node1;
        }
        else if(node2 != null){
            node.next = node2;
        }

        return dummy.next;
    }
}