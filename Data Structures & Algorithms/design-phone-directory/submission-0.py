class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.available = {i for i in range(maxNumbers)}
        self.unavailable = set()

    def get(self) -> int:
        if len(self.available) == 0:
            return -1
        slot = self.available.pop()
        self.unavailable.add(slot)
        return slot
        

    def check(self, number: int) -> bool:
        if number in self.available:
            return True
        return False


    def release(self, number: int) -> None:
        if number not in self.unavailable:
            return
        self.unavailable.remove(number)
        self.available.add(number)

        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
