# 풀이
- LeetCode 75, Medium
- DP - 1D
- Time: 6m 45s
- [2, 1, 1, 2] 케이스 통과못해서 살짝 당황할 뻔 했는데 그려가면서 푸니깐 금방 풀렸음.

## 내 풀이
```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        if n < 3: # 배열 길이가 1,2 면 둘중 큰 값이 정답
            return max(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0]) # 0번째랑 1번째랑 둘중에 큰거
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])  # 현재랑 이전전꺼 합친거 vs 이전꺼 
        return dp[n - 1]
```

## 다른 풀이
### Approach 1: Recursion with Memoization
```py
class Solution:

    def __init__(self):
        # 메모이제이션을 위한 딕셔너리 초기화
        self.memo = {}

    # rob 메서드는 robFrom 메서드가 반환한 최종 최대 이익을 반환합니다. 
    def rob(self, nums: List[int]) -> int:
        # 매번 새롭게 문제를 풀기 위해 메모 초기화
        self.memo = {}

        # 0번째 집부터 시작하여 최대 이익을 계산
        return self.robFrom(0, nums)

    def robFrom(self, i, nums):
        # 더 이상 남은 집이 없을 경우, 0을 반환
        if i >= len(nums):
            return 0

        # 이미 계산된 값이 있는 경우, 캐시된 값을 반환
        if i in self.memo:
            return self.memo[i]

        # 현재 집을 털지 않거나, 다음 집을 건너뛰고 현재 집을 터는 두 가지 경우 중 최대값 계산
        ans = max(
            self.robFrom(i + 1, nums),  # 현재 집을 털지 않고 다음 집으로 이동
            self.robFrom(i + 2, nums) + nums[i]  # 현재 집을 털고 다다음 집으로 이동
        )

        # 계산된 값을 메모에 저장하여 다음에 사용할 수 있도록 함
        self.memo[i] = ans
        return ans
```

### Approach 2: Dynamic Programming
DP 테이블을 사용하여 각 집에서 가능한 최대 이익을 역순으로 계산
```py
class Solution:

    def rob(self, nums: List[int]) -> int:

        # 예외 처리: 빈 배열인 경우, 털 수 있는 집이 없으므로 0 반환
        if not nums:
            return 0

        # 각 인덱스에서 최대 털 수 있는 금액을 저장할 DP 테이블 초기화
        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        N = len(nums)

        # 기본 경우 초기화: 마지막 집을 넘어간 경우에는 0, 마지막 집에서는 그 집의 금액만큼
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]

        # DP 테이블 계산: 뒤에서부터 앞으로 진행
        for i in range(N - 2, -1, -1):
            # 현재 집을 털지 않고 다음 집을 털거나, 현재 집을 털고 다다음 집을 털거나 중에서 큰 값 선택
            maxRobbedAmount[i] = max(
                maxRobbedAmount[i + 1],  # 현재 집을 털지 않고 다음 집으로 이동
                maxRobbedAmount[i + 2] + nums[i]  # 현재 집을 털고 두 칸 건너뛰어 다음 털 수 있는 집으로 이동
            )

        # 0번째 집부터 시작했을 때의 최대 이익 반환
        return maxRobbedAmount[0]

```

### Approach 3: Optimized Dynamic Programming
```py
class Solution:

    def rob(self, nums: List[int]) -> int:

        # 예외 처리: 빈 배열인 경우, 털 수 있는 집이 없으므로 0 반환
        if not nums:
            return 0

        N = len(nums)

        # rob_next_plus_one: 현재 집 다음 두 번째 집부터의 최대 이익
        # rob_next: 다음 집부터의 최대 이익
        rob_next_plus_one = 0
        rob_next = nums[N - 1]

        # DP 계산: 뒤에서부터 앞으로 진행
        for i in range(N - 2, -1, -1):

            # 현재 집에서 얻을 수 있는 최대 이익 계산
            current = max(rob_next, rob_next_plus_one + nums[i])

            # 변수를 업데이트: 다음 반복을 위해 현재 값을 저장
            rob_next_plus_one = rob_next
            rob_next = current

        # 0번째 집부터 시작했을 때의 최대 이익 반환
        return rob_next

```