import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
      pq = []
      for elem, nums in Counter(s).items():
        heapq.heappush(pq, (-nums, elem))
        
      answer = []
      while pq:
        first_pop_num, first_pop_elem = heapq.heappop(pq)
        if len(answer) == 0 or answer[-1] != first_pop_elem: # 마지막에 넣은거랑 다른거면
          answer.append(first_pop_elem)
          if first_pop_num != -1: # 하나만 남은게 아니라면 
            heapq.heappush(pq, (first_pop_num +1, first_pop_elem))
        else: # 마지막에 넣은거랑 같은거면
          if len(pq) == 0: # 마지막에 넣은거랑 다른거 넣어야하는데 더 꺼낼게 없으면 reorganize 못하는경우니깐 "" 리턴
            return ""

          second_pop_num, second_pop_elem = heapq.heappop(pq) # 한번 더 꺼내서
          answer.append(second_pop_elem) 
          if second_pop_num != -1: # 하나만 남은게 아니라면 다시 넣어줘야함
            heapq.heappush(pq, (second_pop_num + 1, second_pop_elem))
          heapq.heappush(pq, (first_pop_num, first_pop_elem))
          
          
      return "".join(answer)