​# 풀이
- Difficulty: Easy
- Topic:  Array / String 
- Elapsed Time:  2m
- Status:  O (2 times)
- Memo: 처음 풀었을때 복기를 안해서 그런지 어떻게 풀었는지 기억이 안났음

## 내 풀이

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0  # 최대 수익
        min_price = math.inf  # 최소 값

        for p in prices:
            if p < min_price:
                # min_price 보다 더 작은게 나왔으면 min 갱신
                min_price = p
            elif p - min_price > max_profit:
                # 현재 가격 - min_price 가 max_profit 보다 크면, max_profit 갱신
                max_profit = p - min_price
        return max_profit
```

## 다른 풀이
### Approach 1: Brute Force
Brute Force 로 푸는 법
```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

        return max_profit
```

### Approach 2: One Pass
내 코드와 똑같다.
```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit
```
