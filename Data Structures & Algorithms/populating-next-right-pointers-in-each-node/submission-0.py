class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = collections.deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i < level_size - 1:
                    nxt = queue[0]
                    node.next = nxt
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root