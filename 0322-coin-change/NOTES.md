# 풀이
- Difficulty:  Medium
- Topic:  1D DP
- Elapsed Time:  15m
- Status:  O 
- Approach:  작은 문제(dp[a-c])의 해를 이용해 큰 문제(dp[a])를 해결할 수 있다는 생각으로 dp로 접근했다.
- Memo:  이전에 그리드로 풀려다가 시간초과 발생해서 못풀었던 문제.

## 내 풀이
```py
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)  # dp 초기화
        dp[0] = 0

        coins.sort()

        for c in coins:  # 동전 c를 사용할 수 있는 최소 금액 c부터 시작
            # 현재 금액 a를 만들기 위해 최소 동전 개수 갱신
            for a in range(c, amount + 1):
                # dp[a - c] + 1: a - c원을 만들 수 있다면, c를 추가해서 만들 수 있음
                dp[a] = min(dp[a], dp[a - c] + 1)

        return -1 if dp[amount] == math.inf else dp[amount]
```

## 다른 풀이
### Approach 1 (Dynamic programming - Top down) [Accepted]
깊이 우선 탐색(DFS)와 메모이제이션을 활용하여 동전 교환 문제를 해결합니다. lru_cache 데코레이터를 사용해 중복 계산을 피하고, 각 서브 문제의 결과를 캐싱하여 성능을 최적화합니다.
```py
from functools import lru_cache


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # 재귀 함수 dfs에 메모이제이션을 적용하여 결과를 캐싱합니다.
        @lru_cache(None)
        def dfs(rem):
            # 남은 금액이 음수면 불가능하므로 -1을 반환합니다.
            if rem < 0:
                return -1
            # 남은 금액이 0이면 필요한 동전 개수는 0입니다.
            if rem == 0:
                return 0
            
            # 최소 동전 개수를 초기화합니다.
            min_cost = float('inf')
            # 각 동전에 대해 dfs 호출을 통해 남은 금액을 계산합니다.
            for coin in coins:
                res = dfs(rem - coin)
                # 결과가 유효한 경우(즉, -1이 아닌 경우) 최소값을 갱신합니다.
                if res != -1:
                    min_cost = min(min_cost, res + 1)
            
            # 최종적으로 최소 동전 개수가 inf가 아니면 반환하고, 그렇지 않으면 -1을 반환합니다.
            return min_cost if min_cost != float('inf') else -1

        # 목표 금액에 대해 dfs 함수를 호출합니다.
        return dfs(amount)
```

### Approach 2 (Dynamic programming - Bottom up) [Accepted]
내가 참고한 방식
```py
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 
```

### Approach 3 (Brute force) [Time Limit Exceeded]
DFS로 동전 교환 문제를 해결하지만, 모든 경우를 탐색하여 시간이 오래 걸리기 때문에 시간 초과가 발생함
```py
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        def dfs(idx, amount):
            # 남은 금액이 0이면 동전이 필요하지 않으므로 0을 반환합니다.
            if amount == 0:
                return 0
            # 동전을 전부 사용했거나 남은 금액이 양수일 때만 계산합니다.
            if idx < n and amount > 0:
                # 최소 동전 개수를 무한대 값으로 초기화합니다.
                min_cost = float('inf')
                # 현재 동전으로 만들 수 있는 경우의 수를 모두 시도합니다.
                for x in range(0, amount // coins[idx] + 1):
                    # 현재 동전을 x개 사용할 경우를 재귀적으로 탐색합니다.
                    res = dfs(idx + 1, amount - x * coins[idx])
                    # 결과가 유효한 경우 최소값을 갱신합니다.
                    if res != -1:
                        min_cost = min(min_cost, res + x)
                # min_cost가 갱신되지 않았다면 -1을 반환하고, 그렇지 않으면 최소값을 반환합니다.
                return -1 if min_cost == float('inf') else min_cost
            return -1

        # 시작 인덱스 0과 목표 금액을 인수로 하여 dfs 호출
        return dfs(0, amount)
```