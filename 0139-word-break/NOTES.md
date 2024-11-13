# 풀이
- Medium
- DP
- Time: X
- dp 로 그럴싸하게 풀었는데 s="bbbbbbb", worddict=["bbb", "bbbb"] 이 케이스에서 걸려서 못품

## 다른 풀이
### Approach 1: Breadth-First Search
s 의 각 문자들을 노드로 생각해서 **너비 우선 탐색(BFS)**을 사용하여 문자열을 사전의 단어들로 분할할 수 있는지 확인하는 방식
```py
from collections import deque
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordDict를 집합으로 변환하여 빠르게 검색할 수 있도록 함
        words = set(wordDict)
        # 시작 위치를 저장하는 큐, 0부터 시작
        queue = deque([0])
        # 방문한 인덱스를 저장하는 집합
        seen = set()

        # 큐가 비어있지 않을 때까지 반복
        while queue:
            # 큐의 맨 앞 요소를 꺼내서 시작 위치로 설정
            start = queue.popleft()
            # 문자열의 길이에 도달했다면 True 반환
            if start == len(s):
                return True

            # start부터 끝까지 모든 end 위치 탐색
            for end in range(start + 1, len(s) + 1):
                # 이미 방문한 end 위치는 건너뜀
                if end in seen:
                    continue

                # 부분 문자열이 words에 있다면 큐에 추가하고 방문 표시
                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)

        # 문자열을 완전히 분할할 수 없다면 False 반환
        return False

```

### Approach 2: Top-Down Dynamic Programming
탑다운 방식은 이해 못했음
```py
from functools import cache
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 메모이제이션을 위한 캐시 적용
        @cache
        def dp(i):
            # i가 0보다 작아졌다면 문자열을 완전히 분할할 수 있다는 의미이므로 True 반환
            if i < 0:
                return True

            # wordDict에 있는 각 단어를 확인
            for word in wordDict:
                # 현재 위치에서 word 길이만큼 이전의 부분 문자열이 word와 일치하는지 확인
                if s[i - len(word) + 1 : i + 1] == word and dp(i - len(word)):
                    return True  # 유효한 분할이 가능하다면 True 반환

            return False  # 모든 단어를 확인해도 분할이 불가능하면 False 반환

        # 전체 문자열이 분할 가능한지 확인하여 결과 반환
        return dp(len(s) - 1)

```

### Approach 3: Bottom-Up Dynamic Programming
```py
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp 배열을 생성하여 부분 문자열의 분할 가능 여부를 기록
        dp = [False] * len(s)
        
        # 문자열의 각 인덱스에 대해 확인
        for i in range(len(s)):
            # wordDict에 있는 각 단어에 대해 확인
            for word in wordDict:
                # 현재 인덱스가 단어의 길이보다 짧으면 건너뜀
                if i < len(word) - 1:
                    continue

                # i가 단어의 끝에 해당하거나, 이전 인덱스에서 분할이 유효한 경우
                if i == len(word) - 1 or dp[i - len(word)]:
                    # 부분 문자열이 해당 단어와 일치하면 dp[i]를 True로 설정
                    if s[i - len(word) + 1 : i + 1] == word:
                        dp[i] = True
                        break

        # 최종적으로 문자열 끝까지 분할이 가능한지 여부를 반환
        return dp[-1]

```

### Approach 4: A Different DP
**동적 계획법(Dynamic Programming)**을 사용하여 문자열 s가 wordDict에 있는 단어들로 분할될 수 있는지 확인합니다. 이 접근법은 슬라이딩 윈도우 기법을 통해 부분 문자열을 확인하면서 dp 테이블을 채웁니다.
```py
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 문자열의 길이를 저장
        n = len(s)
        # wordDict를 집합으로 변환하여 검색을 빠르게 함
        words = set(wordDict)
        # dp 배열을 생성하여 분할 가능 여부를 저장, dp[0]은 빈 문자열이므로 True
        dp = [False] * (n + 1)
        dp[0] = True

        # i는 부분 문자열의 끝 위치를 나타냄
        for i in range(1, n + 1):
            # j는 부분 문자열의 시작 위치를 나타냄
            for j in range(i):
                # j까지의 부분 문자열이 유효하고, j에서 i까지의 부분 문자열이 words에 있는지 확인
                if dp[j] and s[j:i] in words:
                    dp[i] = True  # i까지의 부분 문자열이 유효하게 분할될 수 있음을 표시
                    break  # 더 이상 확인할 필요가 없으므로 루프 종료

        # 전체 문자열이 분할 가능한지 여부를 반환
        return dp[-1]

```