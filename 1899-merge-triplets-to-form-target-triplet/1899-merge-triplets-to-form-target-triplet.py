from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        complete_idx = set()
        
        for t in triplets:
            # 하나라도 큰게 있으면 못합치니깐 패스
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]: 
                continue
            for idx in range(3):
                if t[idx] == target[idx]: # 하나씩 비교해보고 target이랑 똑같으면 그 인덱스 추가
                    complete_idx.add(idx)
        
        if len(complete_idx) == 3:
            return True
        return False