from typing import Counter, List
import heapq


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        q = []
        c = Counter(arr)

        for num in c:
            heapq.heappush(q, (c[num], num))  # 개수랑 숫자

        while k > 0:
            cnt, num = heapq.heappop(q)

            if cnt > k:
                return len(q) + 1
            elif cnt == k:
                return len(q)
            else:
                k -= cnt

        return len(q)