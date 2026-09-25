class RandomizedSet:

    def __init__(self):
        self.random_map = {}
        self.arr = []
        self.end = -1

    def insert(self, val: int) -> bool:
        if val in self.random_map:
            return False
        
        # insert into array first:
        self.end += 1
        self.arr.append(val)

        # insert into the map
        self.random_map[val] = self.end

        return True

    def remove(self, val: int) -> bool:
        if val not in self.random_map:
            return False
        
        # remove from the arr (replace the element from the array)
        i = self.random_map[val]
        last_elem = self.arr[-1]

        # update the index i with the last element
        self.arr[i] = last_elem
        self.random_map[last_elem] = i
        
        # remove last element from arr and val from map
        self.arr.pop()
        del self.random_map[val]
        self.end -= 1
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)