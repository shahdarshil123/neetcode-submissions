class LFUCache:

    def __init__(self, capacity: int):
        self.lfuMap = {1: LinkedList()}
        self.nodeMap = {}
        self.minFreq = 1
        self.capacity = capacity

    def _update(self, node):
        freq = node.used
        self.lfuMap[freq].remove(node)
        if freq == self.minFreq and self.lfuMap[freq].isEmpty():
            self.minFreq += 1
        node.used += 1
        if node.used not in self.lfuMap:
            self.lfuMap[node.used] = LinkedList()
        self.lfuMap[node.used].add_to_mru(node)

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.value = value
            self._update(node)
        else:
            if len(self.nodeMap) == self.capacity:
                lru_node = self.lfuMap[self.minFreq].remove_from_lru()
                if lru_node:
                    del self.nodeMap[lru_node.key]
            
            node = Node(key, value, 1)
            self.nodeMap[key] = node
            self.minFreq = 1
            if 1 not in self.lfuMap:
                self.lfuMap[1] = LinkedList()
            self.lfuMap[1].add_to_mru(node)

class LinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        previous = node.prev
        nxt = node.next
        previous.next = nxt
        nxt.prev = previous
        node.next = None
        node.prev = None
    
    def add_to_mru(self, node):
        mru = self.tail.prev
        mru.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = mru

    def remove_from_lru(self):
        if self.isEmpty(): return None
        node = self.head.next
        self.remove(node)
        return node

    def isEmpty(self):
        return self.head.next == self.tail

class Node:
    def __init__(self, key=-1, value=-1, used=0):
        self.key = key
        self.value = value
        self.used = used
        self.next = None
        self.prev = None