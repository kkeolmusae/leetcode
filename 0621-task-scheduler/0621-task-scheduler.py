from collections import defaultdict
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = defaultdict(int)

        for t in tasks:  # 알파벳 별로 개수 넣고
            dic[t] += 1

        q = [-d for d in dic.values()]  # 알파벳별 개수를 -로 바꿔서 (max heap)
        heapq.heapify(q)  # heapq 로 만들기

        time = 0
        while q:
            cycle = n + 1  # 한 사이클 제한
            stores = []
            task = 0  # 한 사이클에 처리한 일감

            while cycle > 0 and q:
                current = -heapq.heappop(q)  # 하나 꺼내서
                if current > 1:  # 다음에 또 처리해야하는거면 stores에 임시로 넣어두고
                    stores.append(-(current - 1))
                cycle -= 1
                task += 1

            for num in stores:  # 다음에 처리해야하는 task들 q에 넣기
                heapq.heappush(q, num)

            if not q:  # 다음에 처리할 task 가 없는 경우 -> 끝난거니깐 이번에 처리한 task 만큼 시간 증가
                time += task
            else: # 다음에 처리할 task 가 있는 경우 -> 아직 안끝난거니깐 사이클만큼 시간 증가
                time += n + 1
        return time