from typing import List
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck_size = len(deck)
        if deck_size == 1:
            return deck
        
        deck.sort() # 오름차순 정렬
        q = deque()
        
        while deck:
            if len(q) == 0:
                q.append(deck.pop())
                
            q.appendleft(q.pop())
            q.appendleft(deck.pop())
        
        return q