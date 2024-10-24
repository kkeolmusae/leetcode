# 풀이
- NeetCode 150, Medium
- DP 
- Time: X
- 배열이 사실 원형으로 이어져 있는 문제를 풀때 접근 방법은 생각이 났는데 (앞->뒤, 뒤->앞 두번 계산해서 풀거나, 배열 뒤에 똑같은 배열을 붙여서 푸는 방식), 방법이 안떠올라서 설명보고 이해함

## 내 풀이
- robs 코드는 이전에 house robber 1 에서 사용한코드 그대로 썼고, 결과 return 할때 max(첫번째 집을 제외하고 앞->뒤, 마지막 집 제외하고 뒤 -> 앞) 으로 품. 
- 첫번째 집을 제외하는 이유는 첫번째 집을 선택하지 않고 마지막 집을 선택하는 케이스에 대응한 것이고,
- 마지막 집을 제외하는 이유는 마지막 집을 선택하지 않고 첫번째 집을 선택하는 케이스에 대응하기 위함.
```py
class Solution:
    def robs(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        if n < 3:
            return max(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n - 1]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        # 첫 번째 집을 털고 마지막 집을 털지 않는 경우와,
        # 첫 번째 집을 털지 않고 마지막 집을 털 수 있는 경우 중 최대 금액 선택
        # 외냐하면 첫번째집이랑 마지막 집이 이어져있다는 조건이 있기 떄문
        return max(self.robs(nums[1:]), self.robs(list(reversed(nums))[1:]))
```

## 다른 풀이
### Approach 1: Dynamic Programming
```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    def rob_simple(self, nums: List[int]) -> int:
        t1 = 0
        t2 = 0
        for current in nums:
            temp = t1
            t1 = max(current + t2, t1)
            t2 = temp

        return t1
```