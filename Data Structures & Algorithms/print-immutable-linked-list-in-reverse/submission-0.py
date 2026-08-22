class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        node = head
        stack = []

        while node:
            stack.append(node)
            node = node.getNext()
        
        while stack:
            node = stack.pop()
            node.printValue()
        
