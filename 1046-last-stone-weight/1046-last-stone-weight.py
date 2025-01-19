class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []
        for s in stones:
            heapq.heappush(q, -s)

        while len(q) > 1:
            a = -heapq.heappop(q)
            b = -heapq.heappop(q)

            if a > b:
                heapq.heappush(q, -(a - b))
            elif a < b:
                heapq.heappush(q, -(b - a))

        return 0 if not len(q) else -q[0]