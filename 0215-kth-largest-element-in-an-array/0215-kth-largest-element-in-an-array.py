class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            heapq.heappush(q, num)  # 일단 넣고

            if len(q) > k:  # k개 보다 크면 pop해서 k개 까지만 넣어두면
                heapq.heappop(q)
        return q[0]  # q[0]에 있는 값이 k번째로 큰 값