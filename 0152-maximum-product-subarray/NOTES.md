# 풀이
- Neetcode 150, Medium
- DP
- Time: x
- 브루트포스로 풀기 싫어서 삽질하다가 시간 오바남

## 내 풀이
```py
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 현재까지의 최소 곱과 최대 곱을 각각 min_num, max_num에 저장합니다.
        min_num = nums[0]
        max_num = nums[0]

        # 최종 결과로 최대 곱을 저장할 변수 result를 초기화합니다.
        result = nums[0]
        
        # 배열의 두 번째 원소부터 순회합니다.
        for i in range(1, len(nums)):
            num = nums[i]
            
            # 현재 원소 num과 기존 min_num, max_num에 num을 곱한 값들 중에서
            # 최소값과 최대값을 구합니다.
            t_min_num = min(num, min_num * num, max_num * num)
            t_max_num = max(num, max_num * num, min_num * num)
            
            # 계산된 최소값과 최대값을 각각 min_num과 max_num에 업데이트합니다.
            min_num = t_min_num
            max_num = t_max_num
            
            # 현재까지의 최대 곱인 max_num과 result 중 더 큰 값을 result에 저장합니다.
            result = max(max_num, result)
        
        # 최대 곱을 반환합니다.
        return result

```

## 다른 풀이
### Approach 1: Brute Force (Python TLE)
```py
class Solution:
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0

        result = nums[0]

        for i in range(len(nums)):
            accu = 1
            for j in range(i, len(nums)):
                accu *= nums[j]
                result = max(result, accu)

        return result
```

### Approach 2: Dynamic Programming
내 코드에서 변수활용만 조금 다름. (사실 이거 보고 좀 참고함ㅋ)
```py
class Solution:
    def maxProduct(self, nums):
        # 배열이 비어있는 경우 0을 반환합니다.
        if len(nums) == 0:
            return 0

        # 현재까지의 최대 곱과 최소 곱을 초기화합니다.
        max_so_far = nums[0]
        min_so_far = nums[0]
        
        # 최대 곱의 결과를 저장할 변수를 초기화합니다.
        result = max_so_far

        # 두 번째 원소부터 순회합니다.
        for i in range(1, len(nums)):
            curr = nums[i]
            
            # 임시 변수로 현재 원소와 곱한 값 중 최대값을 구합니다.
            temp_max = max(curr, max(max_so_far * curr, min_so_far * curr))
            
            # 현재 원소와 곱한 값 중 최소값을 구해 min_so_far에 저장합니다.
            min_so_far = min(curr, min(max_so_far * curr, min_so_far * curr))

            # max_so_far는 temp_max로 업데이트하여 최대값을 유지합니다.
            max_so_far = temp_max
            
            # result를 현재까지의 최대 곱과 비교하여 더 큰 값으로 업데이트합니다.
            result = max(max_so_far, result)

        # 최대 곱을 반환합니다.
        return result

```

### Approach 3:
```py
```