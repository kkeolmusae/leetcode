from collections import defaultdict
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = defaultdict(int)
        for num in nums:
            dict[num] += 1
        
        hq = []
        for key in dict:
            heapq.heappush(hq, (-dict[key], key))
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(hq)[1])

        return result