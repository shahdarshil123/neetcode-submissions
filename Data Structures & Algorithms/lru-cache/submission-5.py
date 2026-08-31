class Node:
    def __init__(self, key = -1, value = -1):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used = 0
        self.dummy = Node()
        self.tail = Node()
        self.dummy.next = self.tail
        self.tail.prev = self.dummy
        self.nodeMap = {}

    def _remove(self, node):
        prev_node = node.prev
        nxt_node = node.next
        prev_node.next = nxt_node
        nxt_node.prev = prev_node

    def _add_to_tail(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self._remove(node)
        self._add_to_tail(node)
        return node.value
 
    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.value = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            if self.used == self.capacity:
                lru = self.dummy.next
                del self.nodeMap[lru.key]
                self._remove(lru)
                self.used -= 1
            node = Node(key, value)
            self.nodeMap[key] = node
            self._add_to_tail(node)
            self.used += 1