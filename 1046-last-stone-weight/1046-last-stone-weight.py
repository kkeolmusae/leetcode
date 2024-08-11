import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []
        for s in stones:
            heapq.heappush(q, -s)

        while len(q) >= 2:
            s1 = heapq.heappop(q)
            s2 = heapq.heappop(q)

            if s1 != s2:
                heapq.heappush(q, -abs(s1 - s2))

        if len(q):
            return -q[0]
        return 0