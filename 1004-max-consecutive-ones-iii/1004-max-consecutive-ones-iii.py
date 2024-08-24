from collections import deque
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        q = deque()
        result = 0

        if k == 0:
            cnt = 0
            for n in nums:
                if n == 1:
                    cnt += 1
                else:
                    cnt = 0
                result = max(result, cnt)
        else:
            for n in nums:
                if n == 1:
                    q.append(n)
                else:
                    if k > 0:
                        q.append(n)
                        k -= 1
                    else:
                        while q[0] != 0:
                            q.popleft()  # 1 날리고
                        q.popleft()  # 연결해주던 0 지우고
                        q.append(n)  # 새 0 넣고
                result = max(result, len(q))
        return result