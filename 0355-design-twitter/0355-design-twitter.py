import heapq
class Twitter:

    def __init__(self):
        self.nTime=0
        self.tweetMap=defaultdict(list)
        self.followMap=defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.nTime,tweetId])
        self.nTime-=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        result=[]
        heap=[]
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                idx=len(self.tweetMap[followeeId])-1
                time,tweetId=self.tweetMap[followeeId][idx]
                heap.append([time,tweetId,followeeId,idx-1])
        heapq.heapify(heap)
        while heap and len(result)<10:
            time,tweetId,followeeId,idx=heapq.heappop(heap)
            result.append(tweetId)
            if idx>=0:
                time,tweetId=self.tweetMap[followeeId][idx]
                heapq.heappush(heap,[time,tweetId,followeeId,idx-1])
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)