# 풀이
- Difficulty: Medium
- Topic:  1-D Dynamic Programming
- Elapsed Time:  2m
- Status:  O 
- Memo: 배열이 원형으로 이루어져있을때 배열을 두개 붙이거나 혹은 (앞 -> 뒤), (뒤 -> 앞) 두번 처리하는 방법에 대해서 생각을 해보자

## 내 풀이
rob1 함수는 0198 의 함수를 그대로 사용했다.
```py
class Solution:
    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[n - 1]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return max(nums)
        return max(self.rob1(nums[1:]), self.rob1(list(reversed(nums))[1:]))
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