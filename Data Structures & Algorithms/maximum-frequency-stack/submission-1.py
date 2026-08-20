class FreqStack:

    def __init__(self):
        self.freq_map = {}
        self.count_map = {}
        self.max_count = 0

    def push(self, val: int) -> None:
        self.count_map[val] = self.count_map.get(val,0) + 1
        val_count = self.count_map[val]
        self.max_count = max(self.max_count, val_count)

        if val_count not in self.freq_map:
            self.freq_map[val_count] = []
        
        self.freq_map[val_count].append(val)

    def pop(self) -> int:
        val = self.freq_map[self.max_count].pop()
        self.count_map[val] -= 1
        if not self.freq_map[self.max_count]:
            self.max_count -= 1
        return val