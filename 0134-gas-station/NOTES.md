# 풀이
- Difficulty:  Medium
- Topic:  Array / String
- Elapsed Time:  10m
- Status:  O (1 times)
- Memo: 이전에 못풀었던 문제인데 해설을 좀 외워서 푼 느낌

## 내 풀이
```py
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        curr = 0
        result = 0

        for idx in range(len(gas)):
            used_gas = gas[idx] - cost[idx]
            total += used_gas
            curr += used_gas

            # curr 이 음수면 다음 지역으로 못간다는거임
            if curr < 0:
                curr = 0  # 초기화하고
                result = idx + 1  # 현재 위치에서는 안되는거니깐 다음 위치로 설정

        if total >= 0:  # total이 양수면 모든 지역 다 갈 수 있다는거임
            return result
        return -1

```

## 다른 풀이
### Approach
```py
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 전체 연료 이득을 나타내는 변수
        total_gain = 0
        
        # 현재 경로에서의 연료 이득을 추적하는 변수
        curr_gain = 0
        
        # 가능한 시작 지점을 저장하는 변수
        answer = 0

        # 각 주유소를 순회하며 계산
        for i in range(len(gas)):
            # 각 주유소에서 얻는 연료 이득 (gain[i] = gas[i] - cost[i])
            total_gain += gas[i] - cost[i]
            curr_gain += gas[i] - cost[i]

            # 만약 현재 연료 이득이 음수가 된다면
            # 현재 경로에서는 순환 불가능하므로 초기화 후 다음 주유소를 시작 지점으로 설정
            if curr_gain < 0:
                curr_gain = 0
                answer = i + 1

        # 전체 연료 이득이 0 이상이면 순환 가능, 아니라면 순환 불가능
        return answer if total_gain >= 0 else -1

```
