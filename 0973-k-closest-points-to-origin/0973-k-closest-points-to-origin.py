import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for x, y in points:
            distance = (x**2 + y**2) ** 0.5
            heapq.heappush(q, (distance, [x, y]))

        result = []
        for _ in range(k):
            _, [x, y] = heapq.heappop(q)
            result.append([x, y])
        return result