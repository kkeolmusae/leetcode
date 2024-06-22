from typing import List
from collections import defaultdict


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        cnt = defaultdict(int)
        max_cnt = 0
        max_edge = 0
        
        for a, b in edges:
            cnt[a] += 1
            cnt[b] += 1
            
            if cnt[a] > max_cnt:
                max_cnt = cnt[a]
                max_edge = a
            if cnt[b] > max_cnt:
                max_cnt = cnt[b]
                max_edge = b
        return max_edge