class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []

        for num in nums:
            heapq.heappush(q, num)

            if len(q) > k:
                heapq.heappop(q)

        return heapq.heappop(q)