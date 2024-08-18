# 풀이
## 내 코드
문제 그대로 품

index는 tweetId가 5인 게시물이 생성되고 그 다음에 3인 게시물이 생성될 수 있어서 게시물마다 순서를 넣어서 `getNewsFeed`에서 사용함.

```py
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


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

solution = Twitter()
# print(solution.postTweet(1, 5))  # null
# print(solution.getNewsFeed(1))  # 5
# print(solution.follow(1, 2))  # null
# print(solution.postTweet(2, 6))  # null
# print(solution.getNewsFeed(1))  # [6,5]
# print(solution.unfollow(1, 2))  # null
# print(solution.getNewsFeed(1))  # [5]

# print(solution.postTweet(1, 5))  # null
# print(solution.postTweet(1, 3))  # null
# print(solution.getNewsFeed(1))  # [5, 3]

print(solution.postTweet(1, 4))  # null
print(solution.postTweet(2, 5))  # null
print(solution.unfollow(1, 2))  # null
print(solution.getNewsFeed(1))  # [5]

```