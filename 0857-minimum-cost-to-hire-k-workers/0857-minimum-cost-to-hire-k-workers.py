from typing import List
import heapq


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        n = len(quality)

        wage_to_quality_ratio = [
            (wage[idx] / quality[idx], quality[idx]) for idx in range(n)
        ]  # (퀄리티당 임금, 임금) 쌍
        wage_to_quality_ratio.sort()  # 단가 좀 싼애부터

        min_wage = 1e9
        total_quality = 0  # 총 퀄리티
        workers = []  # 노동자 (퀄리티 높은 게 앞에 오게 하기 위해서 - 붙여서 넣음)
        for i in range(n):
            wage_to_quality, quality = wage_to_quality_ratio[i]
            heapq.heappush(workers, -quality)
            total_quality += quality

            if len(workers) > k:  # 할당한 노동자가 필요한 노동자보다 많으면
                q = heapq.heappop(workers)  # 퀄리티 높은애부터 삭제
                total_quality += q

            if len(workers) == k:  # 할당한 노동자 = 필요한 노동자 => 계산
                min_wage = min(min_wage, total_quality * wage_to_quality)

        return round(min_wage, 5)