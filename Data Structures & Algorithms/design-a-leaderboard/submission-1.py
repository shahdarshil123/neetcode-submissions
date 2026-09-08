class Leaderboard:

    def __init__(self):
        self.players = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.players[playerId] = self.players.get(playerId, 0) + score

    def top(self, K: int) -> int:
        heap = [(-1*score, playerId)  for playerId, score in self.players.items()]
        heapq.heapify(heap)
        total = 0

        while heap and K > 0:
            score, playerId = heapq.heappop(heap)
            score = -1 * score
            total += score
            K -= 1
        
        return total


    def reset(self, playerId: int) -> None:
        del self.players[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
