class Twitter:

    def __init__(self):
        self.q = defaultdict(list)  # userId 별로 게시물 (max heap)
        self.following = defaultdict(set)  # userId 별로 follow 하고 있는 user
        # 게시물별 id (가장 최신 Tweets -> 가장 오래된 Tweets 로 가져오기 위함)
        self.idx = 0
        self.tweetsCount = 10  # 가져올 트윗 개수

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.q[userId], (self.idx, tweetId))
        self.idx += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        temp = []
        temp += heapq.nlargest(self.tweetsCount, self.q[userId])  # 내꺼 가져오기

        # 내 팔로잉중에 상위 10개씩 가져오기
        for followeeId in self.following[userId]:
            temp += heapq.nlargest(self.tweetsCount, self.q[followeeId])

        # 내 상위 10개 게시물 + 내 팔로잉의 상위 10개 게시물 중에 10개 가져오기
        result = []
        for p in heapq.nlargest(self.tweetsCount, temp):
            result.append(p[1])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)