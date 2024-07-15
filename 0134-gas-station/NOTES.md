## Notes
내 풀이: cost 가 가장 큰 것의 다음 인덱스부터 계산해보고 0보다 작으면 -1을 리턴하고 0보다 크면 그 인덱스를 리턴하는 방법으로 풀려고 했는데 테스트 케이스에서 틀림. (접근 방식이 잘못됨)

```py
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(cost)
        max_gas = 0
        start_idx = 0

        for idx in range(n):
            if max_gas < cost[idx]:
                max_gas = cost[idx]
                start_idx = idx

        start_idx = (start_idx + 1) % n

        remains = gas[start_idx]
        prev_cost = cost[start_idx]
        for idx in range(start_idx + 1, n + start_idx):
            ridx = idx % n
            remains = remains - prev_cost

            if remains <= 0:
                return -1

            remains += gas[ridx]
            prev_cost = cost[ridx]

        remains = remains - cost[(start_idx + n - 1) % n]

        if remains < 0:
            return -1

        return start_idx
```

#### 맞는 풀이
```py
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        curr_gas = 0
        result = 0

        for idx in range(len(gas)):
            total_gas += gas[idx] - cost[idx]
            curr_gas += gas[idx] - cost[idx]

            if curr_gas < 0:
                curr_gas = 0
                result = idx + 1

        if total_gas >= 0:
            return result
        return -1
```
total_gas 랑 curr_gas로 나눠서 curr_gas 가 음수면 다음 스테이션으로 못간다는거라 해당 구간은 패스하고 curr_gas 초기화하고 시작idx (answer)를 +1 해봄. 

total_gas가 음수면 어디서 시작하던 한바퀴 못돈다는거라서 `-1`을 리턴하고,
양수면 시작idx 부터 시작하면 한바퀴돌 수 있다는 거라 시작 idx 리턴함