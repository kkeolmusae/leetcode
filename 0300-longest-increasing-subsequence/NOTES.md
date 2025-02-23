# 풀이
- Difficulty:  Medium
- Topic:  1D DP
- Elapsed Time:  30m
- Status:  X
- Approach:  이전의 결과값으로 현재의 결과값을 구하는(?) 걸 고려하고 DP로 접근했다.
- Memo:  비슷한 유형을 이전에 풀었던 것 같아서 시도했으나 결국 못품

## 내 풀이
처음 O(n)으로 풀어보려고 했는데 예제만 맞고 테스트 케이스는 중간에 틀렸다.
```py
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            # i번째 원소 nums[i] 이전의 모든 원소 nums[j](j < i)를 확인
            for j in range(i):
                # nums[i] > nums[j] 이면 nums[i]를 nums[j] 뒤에 붙일 수 있음
                # 즉, dp[j] + 1을 고려하여 dp[i]를 갱신
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)
```

## 다른 풀이
### Approach 1: Dynamic Programming
```py
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
```

### Approach 2: Intelligently Build a Subsequence
[4,5,6,1,2,3,4] 인 경우 처음에는 sub = [4,5,6] 인데 그 다음엔 [1,5,6] -> [1,2,6] -> [1,2,3] -> [1,2,3,4] 이렇게 바뀜.
```py
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS를 저장할 리스트 (처음에는 첫 번째 원소만 포함)
        sub = [nums[0]]  
        
        for num in nums[1:]:  # nums 배열의 두 번째 원소부터 탐색
            if num > sub[-1]:  
                # 현재 숫자가 sub의 마지막 값보다 크면 증가하는 수열을 확장
                sub.append(num)
            else:
                # 현재 숫자가 sub의 일부 값을 대체할 수 있는 경우
                i = 0
                while num > sub[i]:  
                    i += 1
                sub[i] = num  # 기존 값 교체 (길이 유지)
        
        # 최종적으로 sub의 길이가 LIS의 길이
        return len(sub)
```

### Approach 3: Improve With Binary Search
Approach 2는 교체하는 위치를 찾기위해 while문을 써서 시간 복잡도가 O(n^2) 인데, Approach 3은 이진탐색을 써서 O(nlogn) 으로 해결했다.
```py
from bisect import bisect_left  # 이진 탐색을 위한 라이브러리 추가

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []  # LIS의 길이를 유지하는 리스트

        for num in nums:
            i = bisect_left(sub, num)  # num이 들어갈 위치 찾기 (이진 탐색)

            # num이 sub의 모든 값보다 크면, 새로운 요소 추가 (LIS 길이 증가)
            if i == len(sub):
                sub.append(num)
            else:
                # sub[i]를 num으로 교체 (하지만 길이는 유지됨)
                sub[i] = num
        
        # sub 리스트의 길이가 최장 증가 부분 수열의 길이
        return len(sub)
```