# 풀이
- LeetCode 75, Easy
- DP - 1D
- Time: 3m
- 걍 규칙에 맞게 넣으면 됨.

## 내 풀이
```py
class Solution:
    def tribonacci(self, n: int) -> int:
        # T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
        dp = [0] * (38) # 0 <= n <= 37 이라서 적당히 38 넣고 시작함
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]
```

## 다른 풀이
### Approach 1: Dynamic Programming (Top Down)
TopDown 방식. Top Down 보다 Bottom Up이 익숙한듯..
```py
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {0: 0, 1: 1, 2: 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            dp[i] = dfs(i - 1) + dfs(i - 2) + dfs(i - 3)
            return dp[i]
        
        return dfs(n)
```

### Approach 2: Dynamic Programming (Bottom Up)
내 코드랑 비슷함.
```py
class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        dp = [0] * (n + 1)
        dp[1] = dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]
```

### Approach 3: Better Dynamic Programming (Bottom Up)
좀 기똥찬 방식...
```py
class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        a, b, c = 0, 1, 1
        for _ in range(n - 2):
            a, b, c = b, c, a + b + c
        return c
```