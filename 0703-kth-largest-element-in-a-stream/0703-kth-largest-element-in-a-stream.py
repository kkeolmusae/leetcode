import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.kth = k
        self.q = []

        for num in nums:
            heapq.heappush(self.q, num)  # num 넣고

            # q 크기가 k 보다 큰건 필요없으니깐 k 개 만큼만 남게 pop
            if len(self.q) > k:
                heapq.heappop(self.q)

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)  # 하나 넣고

        if len(self.q) > self.kth:
            heapq.heappop(self.q)
            
        return self.q[0]