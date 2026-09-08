class LRUCache:

    def __init__(self, capacity: int):
        self.nodeMap = {}
        self.capacity = capacity
        self.used = 0
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1

        node = self.nodeMap[key]

        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.nodeMap:
            node = Node(key, value)
            self.nodeMap[key] = node
            self.insert(node)
            self.used += 1
            if self.used > self.capacity:
                lru = self.left.next
                self.remove(lru)
                del self.nodeMap[lru.key]
                self.used -= 1
        else:
            node = self.nodeMap[key]
            node.val = value

            self.remove(node)
            self.insert(node)

    def remove(self, node):
        previous = node.prev
        nxt = node.next

        node.prev = None
        node.next = None

        previous.next = nxt
        nxt.prev = previous
        
        return node
    
    def insert(self, node):
        self.mru = self.right.prev
        self.mru.next = node
        self.right.prev = node

        node.next = self.right
        node.prev = self.mru

        return node

class Node:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

