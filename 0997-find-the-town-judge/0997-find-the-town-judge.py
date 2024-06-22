from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return n
        trust_count = [0] * (n + 1)
        judge = [True] * (n + 1) # 누군가를 믿은적이 있으면 False 처리해서 판사가 아님을 표기
        
        for a, b in trust: # a 가 b를 믿는다
            trust_count[b] += 1
            judge[a] = False
        
        for idx in range(len(judge)):
            if judge[idx] == True and trust_count[idx] == n-1:
                return idx
        return -1