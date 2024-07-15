​
return start_idx
```
​
맞는 풀이
```
from typing import List
​
​
class Solution:
def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
total_gas = 0
curr_gas = 0
result = 0
​
for idx in range(len(gas)):
total_gas += gas[idx] - cost[idx]
curr_gas += gas[idx] - cost[idx]
​
if curr_gas < 0:
curr_gas = 0
result = idx + 1
​
if total_gas >= 0:
return result
return -1
```
total_gas 랑 curr_gas로 나눠서 curr_gas 가 음수면 다음 스테이션으로 못간다는거라 해당 구간은 패스하고 curr_gas 초기화하고 시작idx (answer)를 +1 해봄.
​
total_gas가 음수면 어디서 시작하던 한바퀴 못돈다는거라서 `-1`을 리턴하고,
양수면 시작idx 부터 시작하면 한바퀴돌 수 있다는 거라 시작 idx 리턴함