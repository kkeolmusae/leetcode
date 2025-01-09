# 풀이
- Difficulty:  Medium
- Topic:  Stack
- Elapsed Time:  20m
- Status:  X
- Memo: 이것도 0739 처럼 못풀었다. 이해하고 다시 풀어보니 해결하긴 했다.

## 내 풀이
```py
class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed))  # 자동차 위치랑 속도 묶고 내림차순

        # target에 도달하는데 걸리는 시간 (오름차순으로 되어있음)
        times = [float(target - p) / s for p, s in cars]
        ans = 0

        while len(times) > 1:
            curr = times.pop()  # 제일 빨리 target에 도착하는 차

            # times[-1]: 그 다음으로 도착하는 차
            if times[-1] > curr:  # 못따라잡음
                ans += 1
            else:
                times[-1] = curr  # 합류
        return ans + len(times)
```

## 다른 풀이
### Approach 1: Sort
```py
class Solution(object):
    def carFleet(self, target, position, speed):
        # 자동차의 위치와 속도를 위치 기준으로 정렬
        cars = sorted(zip(position, speed))
        # 각 자동차가 도착하는 데 걸리는 시간을 계산
        times = [float(target - p) / s for p, s in cars]
        ans = 0
        
        # 도착 시간을 비교하여 자동차 무리를 계산
        while len(times) > 1:
            lead = times.pop()  # 가장 마지막 자동차(가장 뒤에 있는 자동차)의 도착 시간
            # 만약 lead 자동차가 앞의 자동차보다 먼저 도착하면 (합쳐지지 않음)
            if lead < times[-1]: 
                ans += 1  # 새로운 자동차 무리로 계산
            else: 
                times[-1] = lead  # 합쳐지는 경우, 무리의 도착 시간을 갱신

        # 남아 있는 자동차(마지막 자동차 무리)를 포함하여 반환
        return ans + bool(times) # 남아 있는 자동차가 있으면 무리로 간주

```