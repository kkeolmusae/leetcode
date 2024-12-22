
# 풀이
- Difficulty:  Medium
- Topic:  1-D Dynamic Programming
- Elapsed Time: X
- Status:  X
- Memo: 30분 넘어서도 못풀었고, 해설을 봐도 이해를 잘 못했다. 그냥 못했다.

## 내 풀이
해설을 보고 다시 푼 Bottom Up 방법이다.
```py
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        # 모든 숫자의 합이 홀수면 같은 subset 이 두개 안나옴
        if total_sum % 2 != 0:
            return False

        # subset_sum = 만들고자 하는 숫자 (부분수열의 합)
        subset_sum = total_sum // 2
        n = len(nums)

        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            curr = nums[i - 1]  # 현재 숫자
            for j in range(subset_sum + 1):
                if curr > j:  # 현재 숫자 > 만들고자 하는 숫자
                    # 현재 숫자 빼고 이전 숫자들로 j 만들수 있는지
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 현재 숫자 빼고 이전 숫자들로 j 만들 수 있는지,
                    # 또는 이전 숫자들로 (만들고자 하는 수 - 현재 숫자)를 만들 수 있는지
                    # (= 현재 숫자 포함하면 만들고자 하는 수 만들 수 있는지)
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]

        return dp[n][subset_sum]
```

## 다른 풀이
### Approach 1: Top Down Dynamic Programming - Memoization
```py
from functools import lru_cache

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        @lru_cache(maxsize=None)  # 메모이제이션을 위한 데코레이터 (중복 계산 방지)
        def dfs(nums: tuple[int], n: int, subset_sum: int) -> bool:
            # 기본 종료 조건
            if subset_sum == 0:  # 목표 합을 정확히 달성한 경우
                return True
            if n == 0 or subset_sum < 0:  # 숫자가 더 없거나 목표 합을 초과한 경우
                return False
            
            # 현재 숫자를 포함하거나 포함하지 않는 두 가지 경우를 탐색
            result = (dfs(nums, n - 1, subset_sum - nums[n - 1])  # 현재 숫자 포함
                      or dfs(nums, n - 1, subset_sum))            # 현재 숫자 미포함
            return result

        # 배열의 전체 합 계산
        total_sum = sum(nums)

        # 전체 합이 홀수면 두 부분집합으로 나눌 수 없음
        if total_sum % 2 != 0:
            return False

        # 부분집합의 목표 합 계산
        subset_sum = total_sum // 2
        n = len(nums)
        
        # 메모이제이션 DFS 시작
        return dfs(tuple(nums), n - 1, subset_sum)

```

### Approach 2: Bottom Up Dynamic Programming
```py
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # 배열 요소의 전체 합 계산
        total_sum = sum(nums)

        # 전체 합이 홀수인 경우 두 부분집합으로 나눌 수 없음
        if total_sum % 2 != 0:
            return False

        # 목표로 하는 부분집합 합 (전체 합의 절반)
        subset_sum = total_sum // 2
        n = len(nums)

        # DP 테이블 초기화: (n+1) x (subset_sum+1) 크기의 2차원 리스트
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]

        # 초기 조건: 부분집합 합이 0인 경우는 항상 가능 (숫자를 선택하지 않음)
        dp[0][0] = True

        # DP 테이블 채우기
        for i in range(1, n + 1):  # 1번 숫자부터 n번 숫자까지 처리
            curr = nums[i - 1]  # 현재 숫자
            for j in range(subset_sum + 1):  # 목표 합 0부터 subset_sum까지 확인
                if j < curr:  
                    # 현재 숫자를 사용할 수 없는 경우 (목표 합보다 크다면 포함 불가)
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 현재 숫자를 포함하거나 포함하지 않은 두 가지 경우 중 하나라도 가능하면 True
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]

        # 최종 결과 반환: n개의 숫자를 사용하여 subset_sum을 만들 수 있는지 확인
        return dp[n][subset_sum]

```

### Approach 3: Optimised Dynamic Programming - Using 1D Array
```py
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # 배열의 전체 합을 계산
        total_sum = sum(nums)

        # 전체 합이 홀수라면 두 부분집합으로 나눌 수 없음
        if total_sum % 2 != 0:
            return False
        
        # 부분집합의 목표 합 (전체 합의 절반)
        subset_sum = total_sum // 2

        # 부분집합 합을 저장하는 DP 배열 초기화
        dp = [False] * (subset_sum + 1)
        dp[0] = True  # 합이 0인 부분집합은 항상 가능 (아무것도 선택하지 않을 때)

        # 배열의 각 숫자에 대해 DP 배열 갱신
        for curr in nums:
            # 현재 숫자를 사용하여 DP 갱신 (역순으로 탐색)
            for j in range(subset_sum, curr - 1, -1):
                # 현재 숫자를 사용하거나 사용하지 않은 경우 중 하나라도 참이면 갱신
                # (부분집합이 두개기 때문에 사용하거나 안하거나 두가지를 고려한 방법)
                dp[j] = dp[j] or dp[j - curr]

        # 목표 합을 만들 수 있는지 확인
        return dp[subset_sum]
```