import heapq as h 
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = [] # (time, tweetId, userId)
        self.users = {}  # user -> {followers}

    def add(self, userId):
        if self.users.get(userId) is None:
            self.users[userId] = set([userId])

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.add(userId)
        self.time += 1 
        h.heappush(self.tweets, (self.time * -1, tweetId, userId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        if not self.tweets:
            return []
        feed = []
        fix = []
        while self.tweets and len(feed) != 10:
            tweet = h.heappop(self.tweets)
            if tweet[2] == userId or tweet[2] in self.users[userId]:
                feed.append(tweet[1])
            fix.append(tweet)

        for item in fix:
            h.heappush(self.tweets, item)

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.add(followerId)
        self.add(followeeId)
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.add(followerId)
        self.add(followeeId)
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        
