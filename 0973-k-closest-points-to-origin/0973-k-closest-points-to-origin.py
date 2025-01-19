class Solution:
    def euclideanDist(self, x, y):
        return math.sqrt((0 - y) ** 2 + (0 - x) ** 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []

        result = []

        for x, y in points:
            r = self.euclideanDist(x, y)
            heapq.heappush(q, (r, (x, y)))

        while k:
            _, (x, y) = heapq.heappop(q)
            result.append([x, y])
            k -= 1
        return result