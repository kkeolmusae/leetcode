# 풀이
- Difficulty:  Medium
- Topic:  Array / String
- Elapsed Time:  15m 
- Status:  X
- Memo: dp로 풀고싶어서 삽질하다가 실패했다. Approach 0과 2의 방법 위주로 습득하자

## 내 풀이
DP 가 아닌 다른 풀이법이다. 현재 값이랑 직전값이랑 차이가 0보다 크면 그 수만큼 max_profit 에 더해주는 방법으로 하면 답이 나온다.
```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

```

## 다른 풀이
### Approach 0: DP
```py
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        
        # 초기 상태
        hold = -prices[0]  # 첫날 주식을 산 경우 (돈 없는데 샀으니깐 -로 시작)
        not_hold = 0       # 첫날 주식을 사지 않은 경우
        
        # 이전 상태를 기반으로 현재 상태 계산
        for i in range(1, n):
            # 전날에도 주식을 보유한 경우 (hold 유지)
            new_hold = max(hold, not_hold - prices[i])

            # 전날에도 주식을 보유하지 않은 경우 (not_hold 유지).
            # 오늘 주식을 판매한 경우 (hold[i-1] + prices[i])
            new_not_hold = max(not_hold, hold + prices[i])
            
            hold = new_hold
            not_hold = new_not_hold
        
        # 최종적으로 주식을 보유하지 않은 상태가 최대 이익
        return not_hold
```

### Approach 1: Brute Force
```py
class Solution:
    def maxProfit(self, prices):
        # 재귀 호출로 최대 이익 계산 시작
        return self.calculate(prices, 0)

    def calculate(self, prices, s):
        # 시작 인덱스(s)가 배열 길이 이상이면 종료 (더 이상 탐색할 날이 없음)
        if s >= len(prices):
            return 0
        
        # 최대 이익을 저장할 변수 초기화
        max_profit = 0

        # 모든 가능한 매수 시작점을 탐색
        for start in range(s, len(prices)):
            # 현재 매수 시작점에서의 최대 이익 초기화
            max_profit_for_start = 0
            
            # 매수 이후 가능한 모든 매도 날을 탐색
            for i in range(start + 1, len(prices)):
                if prices[start] < prices[i]:  # 매수 가격보다 매도 가격이 높아야 이익 발생
                    # i 이후의 최대 이익 + 현재 거래에서의 이익 계산
                    profit = (
                        self.calculate(prices, i + 1)  # 재귀 호출로 i 이후의 최대 이익 계산
                        + prices[i] - prices[start]  # 현재 매수-매도에서의 이익
                    )
                    # 현재 매수 시작점에서 최대 이익 갱신
                    if profit > max_profit_for_start:
                        max_profit_for_start = profit
            
            # 모든 매수 시작점에 대해 최대 이익 갱신
            if max_profit_for_start > max_profit:
                max_profit = max_profit_for_start
        
        # 최대 이익 반환
        return max_profit

```

### Approach 2: Peak Valley Approach
시간복잡도: O(n), 공간복잡도: O(1)
```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 현재 위치를 나타내는 인덱스
        i = 0
        # 첫날의 가격으로 초기화
        valley = prices[0]  # 계곡 (최소값)
        peak = prices[0]    # 산 (최대값)
        # 최대 이익을 저장할 변수
        maxprofit = 0
        
        # 가격 리스트의 끝까지 탐색
        while i < len(prices) - 1:
            # 가격이 감소하는 구간 찾기 (계곡을 탐색)
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]  # 계곡 값 저장
            
            # 가격이 증가하는 구간 찾기 (산을 탐색)
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]  # 산 값 저장
            
            # 산과 계곡의 차이를 최대 이익에 더함
            maxprofit += peak - valley
        
        # 최대 이익 반환
        return maxprofit

```

### Approach 3: Simple One Pass
내 코드가 여기서 나왔다.
```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxprofit += prices[i] - prices[i - 1]
        return maxprofit
```