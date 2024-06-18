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

#### 분석
<문제 해석>
```
문제는 주어진 정수 배열 deck을 다음과 같은 규칙에 따라 정렬하는 것입니다:

	1.	덱에서 맨 위의 카드를 꺼내서 공개하고 덱에서 제거합니다.
	2.	덱에 카드가 남아 있다면, 덱에서 다음 맨 위의 카드를 덱의 맨 아래로 이동시킵니다.
	3.	덱에 공개되지 않은 카드가 남아 있다면, 1번 단계로 돌아갑니다. 그렇지 않으면 멈춥니다.

이 과정이 끝났을 때 카드들이 오름차순으로 공개되도록 덱을 정렬해야 합니다.

예를 들어, deck = [17, 13, 11, 2, 3, 5, 7]가 주어진 경우, 정
```
즉 위의 1 ~ 3 규칙대로 재정렬했을 때 오름차순 정렬이 되게 하는 deck을 리턴하라는 것이다.
```python
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
```
이게 거의 모범 답안인데 인덱스배열(q)를 왜 사용해서 이렇게 했는지 모르곘음.
