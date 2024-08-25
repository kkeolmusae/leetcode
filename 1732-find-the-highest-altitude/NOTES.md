# 풀이
- LeetCode 75, Easy
- Prefix Sum
- Time: 1m
- 그냥... 쉬움

## 내 풀이
```py
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        start = 0
        for num in gain:
            start += num s# 현재 위치 - 현재 고도
            result = max(result, start)  # 최대 고도 갱신
        return result
```

## 다른 풀이

### Approach: Sliding Window
```py
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 윈도우 내의 0의 개수
        zero_count = 0
        # 가장 긴 윈도우의 길이
        longest_window = 0
        # 윈도우의 왼쪽 끝
        start = 0

        for i in range(len(nums)):
            # 현재 요소가 0이면 zero_count를 증가시킴
            if nums[i] == 0:
                zero_count += 1
            
            # 윈도우 내의 0의 개수가 1을 초과하면 윈도우를 줄임
            while zero_count > 1:
                # 윈도우의 왼쪽 끝이 0이면 zero_count를 감소시킴
                if nums[start] == 0:
                    zero_count -= 1
                # 윈도우의 왼쪽 끝을 오른쪽으로 이동
                start += 1
            
            # 현재 윈도우의 크기를 계산하고, 최댓값을 저장
            longest_window = max(longest_window, i - start)
        
        return longest_window

```