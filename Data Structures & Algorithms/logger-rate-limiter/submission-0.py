class Logger:

    def __init__(self):
        self.logger_map = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.logger_map:
            if self.logger_map[message] + 10 > timestamp:
                return False
        self.logger_map[message] = timestamp
        return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
