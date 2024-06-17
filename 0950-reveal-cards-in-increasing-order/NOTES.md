### NOTES

처음에 아래 코드와 같이 
- 한번은 q의 왼쪽을 팝해서 result에 넣고 그다음에 오른쪽 팝해서 q 왼쪽에 넣고
- 다음에는 q의 오른쪽을 팝해서 Result에 넣고 왼쪽꺼 팝해서 q 오른쪽에 넣고
- 하는 방식으로 했었는데 이러니깐 틀림

Solution 보고도 좀 이해가 안되서 다른 사람들이 보고 푼거 좀 참고해서 수정했는데 어떻게 이렇게 했는지 이해를 못해서 분석 해봐야함

```python
from typing import List
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        result = deque()
        q = deque(sorted(deck))
        flag = True
        
        while len(result) != len(deck):
            if flag:
                card = q.popleft()
                result.append(card)
                if len(q) == 2 and q[0] < q[1]:
                    flag = False
                    continue
                if q:
                    new_card = q.pop()
                    q.appendleft(new_card)
                flag = False
            else:
                card = q.pop()
                result.append(card)
                if len(q) == 2 and q[0] < q[1]:
                    flag = True
                    continue
                if q:
                    new_card = q.popleft()
                    q.append(new_card)
                flag = True
        
        return result
```