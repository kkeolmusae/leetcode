from collections import deque
from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        dq = deque(tokens)
        score = 0
        max_score = 0
      
        while dq:
          if score == 0: # 점수가 없으면 일단 싼거 face up 해야함
            token = dq.popleft()
            if power - token < 0: # 가진 파워 - 사용할 파워 > 0 이면
              return max_score
            score += 1 # 점수 올리고
            power -= token # 파워 낮추고
            max_score = max(max_score, score)
          else:
            if power - dq[0] >= 0: # 파워가 넉넉하면
              token = dq.popleft() # 팝하고 
              power -= token # 파워 낮추고
              score += 1 # 점수 얻기
              max_score = max(max_score, score)
            else: # 파워가 넉넉하지 않으면
              token = dq.pop() # 비싼거 팝하고
              power += token # 파워 올리고
              score -= 1 # 점수 깎고
              
        return max_score