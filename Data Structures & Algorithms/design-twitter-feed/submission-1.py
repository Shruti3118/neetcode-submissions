class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        maxheap = []
        for user in self.followMap[userId]:
            index = len(self.tweetMap[user]) - 1
            if index >= 0:
                count, tweetId = self.tweetMap[user][index]
                maxheap.append([count,tweetId,user,index])
        heapq.heapify(maxheap)
        ans = []
        while maxheap:
            count, tweetId, user, index = heapq.heappop(maxheap)
            ans.append(tweetId)
            if len(ans) == 10:
                break
            if index > 0:
                newCount, newTweetId = self.tweetMap[user][index - 1]
                heapq.heappush(maxheap,[newCount,newTweetId,user,index-1])
        return ans
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
