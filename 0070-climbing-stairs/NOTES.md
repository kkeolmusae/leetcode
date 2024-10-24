# 풀이
- Neetcode 150, Easy
- 1-D Dynamic Programming
- Time: 3m
- 쉬웠음. 

## 내 풀이
```py
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            # (i-1 에서 올라오는 경우) + (i-2 에서 올라오는 경우)
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
```

## 다른 풀이
### Approach 1: Brute Force
피보나치 수열의 변형 문제로, 계단을 오르는 방법을 재귀적으로 계산함
```py
class Solution:
    def climbStairs(self, n: int) -> int:
        # 초기 계단 위치 0에서 시작하여 목표 위치 n까지 도달하는 방법의 수를 계산합니다.
        return self.climb_Stairs(0, n)

    def climb_Stairs(self, i: int, n: int) -> int:
        # 현재 위치 i가 목표 위치 n을 초과하면, 방법이 없으므로 0을 반환합니다.
        if i > n:
            return 0
        # 현재 위치 i가 목표 위치 n과 같으면, 하나의 방법을 찾은 것이므로 1을 반환합니다.
        if i == n:
            return 1
        # 현재 위치에서 한 계단 또는 두 계단을 올라가는 방법의 합을 반환합니다.
        return self.climb_Stairs(i + 1, n) + self.climb_Stairs(i + 2, n)
```

### Approach 2: Recursion with Memoization
```py
class Solution:
    def climbStairs(self, n: int) -> int:
        # 메모이제이션(memoization)을 위한 리스트를 생성하여, 각 위치 i에서 n까지 도달하는 방법의 수를 저장합니다.
        memo = [0] * (n + 1)
        # 초기 위치 0에서 목표 위치 n까지 도달하는 방법의 수를 계산합니다.
        return self.climb_Stairs(0, n, memo)

    def climb_Stairs(self, i: int, n: int, memo: List[int]) -> int:
        # 현재 위치 i가 목표 위치 n을 초과하면, 방법이 없으므로 0을 반환합니다.
        if i > n:
            return 0
        # 현재 위치 i가 목표 위치 n과 같으면, 하나의 방법을 찾은 것이므로 1을 반환합니다.
        if i == n:
            return 1
        # 이미 계산된 값이 memo에 저장되어 있다면, 해당 값을 반환하여 중복 계산을 피합니다.
        if memo[i] > 0:
            return memo[i]
        # 현재 위치에서 한 계단 또는 두 계단을 올라가는 방법의 합을 memo에 저장합니다.
        memo[i] = self.climb_Stairs(i + 1, n, memo) + self.climb_Stairs(i + 2, n, memo)
        # 현재 위치에서 목표 위치까지의 방법의 수를 반환합니다.
        return memo[i]

```

### Approach 3: Dynamic Programming
내 코드랑 거의 똑같음
```py
# Python3
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
```

### Approach 4: Fibonacci Number
변수 두개만 씀.
```py
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 계단이 1개만 있을 경우, 방법은 1가지 뿐이므로 1을 반환합니다.
        if n == 1:
            return 1
        # first와 second는 계단의 첫 번째와 두 번째 방법의 수를 나타냅니다.
        first = 1
        second = 2
        # 3번째 계단부터 n번째 계단까지 방법의 수를 계산합니다.
        for i in range(3, n + 1):
            # 현재 계단에 도달하는 방법의 수는 이전 두 계단의 방법의 합입니다.
            third = first + second
            # first와 second를 한 계단씩 앞으로 이동시킵니다.
            first = second
            second = third
        # n번째 계단에 도달하는 방법의 수를 반환합니다.
        return second

```

### Approach 5: Binets Method
```py
# Python3
class Solution:
    def climbStairs(self, n: int) -> int:
        # 행렬 q를 사용하여 피보나치 수열을 계산합니다.
        q = [[1, 1], [1, 0]]
        # q를 n번 제곱한 결과에서 0번째 행, 0번째 열의 값을 반환합니다.
        res = self.pow(q, n)
        return res[0][0]

    def pow(self, a: [[int]], n: int) -> [[int]]:
        # 단위 행렬을 ret으로 초기화합니다.
        ret = [[1, 0], [0, 1]]
        # n이 0보다 큰 동안 행렬 제곱을 반복합니다.
        while n > 0:
            # n이 홀수인 경우 ret에 a를 곱합니다.
            if (n & 1) == 1:
                ret = self.multiply(ret, a)
            # n을 오른쪽으로 1비트 이동하여 절반으로 줄입니다.
            n >>= 1
            # 행렬 a를 제곱합니다.
            a = self.multiply(a, a)
        return ret

    def multiply(self, a: [[int]], b: [[int]]) -> [[int]]:
        # 두 행렬 a와 b를 곱한 결과를 저장할 행렬 c를 초기화합니다.
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                # 행렬의 곱셈을 수행하여 c의 각 원소를 계산합니다.
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[
```

### Approach 6: Fibonacci Formula
```py
# Python 3
class Solution:
    def climbStairs(self, n: int) -> int:
        # sqrt5는 루트 5의 값을 계산합니다.
        sqrt5 = 5**0.5
        # phi와 psi는 각각 황금비와 그 역을 나타냅니다.
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        # Binet's 공식에 따라 피보나치 수열을 계산하여 n번째 계단의 방법의 수를 반환합니다.
        return int((phi ** (n + 1) - psi ** (n + 1)) / sqrt5)

```