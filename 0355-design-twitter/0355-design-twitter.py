from collections import defaultdict
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.q = defaultdict(list)  # userId 별로 게시물 (max heap)
        self.following = defaultdict(set)  # userId 별로 follow 하고 있는 user
        self.index = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.q[userId], (self.index, tweetId))
        self.index += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = []

        posts += heapq.nlargest(10, self.q[userId])  # 내꺼 10개 추가

        for id in self.following[userId]:  # 내 팔로잉중에
            posts += heapq.nlargest(10, self.q[id])

        result = []
        for p in heapq.nlargest(10, posts):
            result.append(p[1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)