class Twitter:

    def __init__(self):
        self.user_tweet_map = defaultdict(list)
        self.user_follows_map = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp -= 1
        self.user_tweet_map[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        heap.extend(self.user_tweet_map[userId])
        for user in self.user_follows_map[userId]:
            if user != userId:
                heap.extend(self.user_tweet_map[user])
        
        result = []
        heapq.heapify(heap)
        for i in range(10):
            if len(heap) == 0:
                break
            timestamp, tweetId = heapq.heappop(heap)
            result.append(tweetId)
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.user_follows_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follows_map[followerId].discard(followeeId)