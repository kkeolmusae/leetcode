# 풀이
- Difficulty:  Medium
- Topic:  Stack
- Elapsed Time:  20m
- Status:  X
- Memo:  요 근래 푼 Stack 문제 중에 제일 어려웠다. 처음 풀었을때 테스트 케이스는 다 통과했는데 제출했을때 temperatures가 많이 커졌을때 TLE 로 실패했다. Monotonic Stack 에 대해서 확실하게 알면 금방 풀리는 수준의 문제였다.

## 내 풀이
처음에는 O(n^2) 이었어서 TLE 발생했고, 다음 풀이는 Monotonic Stack 에 대해서 이해하고 손코딩 후에 푼 방법이다.
```py
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # 스택: 온도가 높은 날을 찾기 위해 인덱스를 저장
        n = len(temperatures)  # 온도 리스트의 길이
        result = [0] * n  # 결과 리스트 초기화 (모든 값을 0으로 설정)

        for idx in range(n):
            # 스택이 비어 있지 않고, 현재 온도가 스택의 마지막 인덱스 온도보다 높은 경우
            while stack and temperatures[stack[-1]] < temperatures[idx]:
                prev_idx = stack.pop()  # 스택에서 인덱스를 꺼냄
                result[prev_idx] = (
                    idx - prev_idx
                )  # 현재 인덱스와 이전 인덱스의 차이를 결과에 저장

            # 현재 인덱스를 스택에 추가
            stack.append(idx)

        # 최종 결과 반환
        return result
```

## 다른 풀이
### Approach 1: Monotonic Stack
Monotonic Stack 으로 푼 방법이다.
```py
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        
        for curr_day, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        
        return answer
```

### Approach 2: Array, Optimized Space
처음 시도한 접근방법을 개선한 코드이다.
```py
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)  # 온도 리스트의 길이
        hottest = 0  # 지금까지 가장 높은 온도를 기록
        answer = [0] * n  # 결과 리스트 초기화 (모든 값을 0으로 설정)
        
        # 뒤에서 앞으로 순회
        for curr_day in range(n - 1, -1, -1):
            current_temp = temperatures[curr_day]  # 현재 날짜의 온도
            
            # 현재 온도가 지금까지 가장 높은 온도보다 높거나 같으면
            if current_temp >= hottest:
                hottest = current_temp  # 가장 높은 온도를 업데이트
                continue  # 더 따뜻한 날이 없으므로 다음 날로 이동
            
            # 더 따뜻한 날까지의 일수를 계산
            days = 1
            while temperatures[curr_day + days] <= current_temp:
                # answer 배열을 사용해 다음 더 따뜻한 날로 바로 이동
                days += answer[curr_day + days]
            answer[curr_day] = days  # 결과 리스트에 일수를 저장

        return answer  # 최종 결과 반환
```