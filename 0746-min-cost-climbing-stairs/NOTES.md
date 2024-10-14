# 풀이
- LeetCode 75, Easy
- DP - 1D
- Time: 10m?
- DP 문제 안푼지 오래되서 좀 헤맸는데 어찌저찌 푼듯. 막 어렵진 않았다.

## 내 풀이
```py
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = 0
        for idx in range(2, len(cost) + 1):
            # cost[idx - 1] + dp[idx - 1]:  한 단계 전까지의 최소 비용
            # cost[idx - 2] + dp[idx - 2]:  두 단계 전까지의 최소 비용
            dp[idx] = min(cost[idx - 1] + dp[idx - 1], cost[idx - 2] + dp[idx - 2])

        return dp[-1]  # 최소값 리턴
```

## 다른 풀이
### Approach 1: Bottom-Up Dynamic Programming (Tabulation)
오 내 코드랑 거의 똑같음
```py
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 비용 배열의 길이보다 1 더 긴 배열을 생성하여 최소 비용을 저장
        # 이는 마지막 계단을 "최상층"으로 간주하여 도달할 수 있도록 하기 위함
        minimum_cost = [0] * (len(cost) + 1)
        
        # 0번과 1번 계단의 최소 비용은 0이므로, 2번 계단부터 계산 시작
        for i in range(2, len(cost) + 1):
            # 한 계단 오르는 경우의 비용 계산
            take_one_step = minimum_cost[i - 1] + cost[i - 1]
            # 두 계단 오르는 경우의 비용 계산
            take_two_steps = minimum_cost[i - 2] + cost[i - 2]
            # 두 가지 경우 중 더 작은 값을 선택하여 최소 비용 저장
            minimum_cost[i] = min(take_one_step, take_two_steps)

        # 최소 비용 배열의 마지막 요소가 최상층에 도달하는 최소 비용을 나타냄
        return minimum_cost[-1]

```

### Approach 2: Top-Down Dynamic Programming (Recursion + Memoization)
역시 탑다운 방식은 아직 익숙하지 않다...
```py
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minimum_cost(i):
            # 기본 케이스: 0번 또는 1번 계단에서 시작할 수 있음
            if i <= 1:
                return 0

            # 이미 계산된 최소 비용이 있는지 확인
            if i in memo:
                return memo[i]

            # 계산된 값이 없으면, 최소 비용을 계산하여 메모에 저장하고 반환
            down_one = cost[i - 1] + minimum_cost(i - 1)  # 한 계단 내려오는 경우의 비용
            down_two = cost[i - 2] + minimum_cost(i - 2)  # 두 계단 내려오는 경우의 비용
            memo[i] = min(down_one, down_two)  # 더 작은 비용을 선택하여 메모에 저장
            return memo[i]

        memo = {}  # 메모이제이션을 위한 딕셔너리 초기화
        return minimum_cost(len(cost))  # 마지막 계단까지의 최소 비용 계산

```

### Approach 3: Bottom-Up, Constant Space
```py
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:        
        # down_one: 한 계단 전에서 도달한 최소 비용
        # down_two: 두 계단 전에서 도달한 최소 비용
        down_one = down_two = 0
        
        # 2번 계단부터 마지막 계단 다음 위치까지 반복
        for i in range(2, len(cost) + 1):
            temp = down_one  # 현재 down_one 값을 임시로 저장
            # 한 계단 전에서 오르거나, 두 계단 전에서 오르는 두 경우 중 최소 비용 선택
            down_one = min(down_one + cost[i - 1], down_two + cost[i - 2])
            down_two = temp  # 이전 down_one 값을 down_two로 업데이트

        # 최상층에 도달하는 최소 비용 반환
        return down_one

```