from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()  # 1. 덱을 오름차순으로 정렬
        q = deque(range(len(deck)))  # 2. 인덱스를 저장하는 덱 초기화
        
        result = [0] * len(deck)  # 결과를 저장할 리스트 초기화
        
        for card in deck:  # 3. 각 카드에 대해
            result[q.popleft()] = card  # 4. 맨 위 인덱스 위치에 현재 카드 배치
            if q:  # 5. 아직 인덱스가 남아 있다면
                q.append(q.popleft())  # 6. 맨 위 인덱스를 맨 아래로 이동
        
        return result  # 7. 결과 반환