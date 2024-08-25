# 풀이
- LeetCode 75, Medium
- Sliding Window
- Time: 17m
- Sliding Window 방식으로 해결...한것 같기도 하고 아닌것 같기도하고... 문제 방향을 생각하는데 시간이 좀 걸림

## 내 풀이
```py
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0  # 윈도우의 왼쪽 경계
        right = 0  # 윈도우의 오른쪽 경계
        zero_idx = -1  # 마지막으로 만난 0의 인덱스
        result = 0  # 가장 긴 부분 배열의 길이

        for idx in range(len(nums)):

            num = nums[idx]
            if num != 1:  # 0을 만난 경우
                if zero_idx >= 0:  # 이전에 0을 이미 만났다면, 윈도우의 왼쪽 경계를 갱신
                    left = zero_idx + 1  # left를 마지막으로 만난 0의 다음 위치로 이동
                zero_idx = idx  # 현재 0의 인덱스를 기록
            right += 1  # 윈도우의 오른쪽 경계를 늘림

            # 현재 윈도우 크기에서 -1을 한 값(0 또는 1을 하나 제거했을 때의 길이)과 이전의 최댓값을 비교하여 갱신
            result = max(result, (right - left) - 1)

        return result  # 가장 긴 부분 배열의 길이 반환

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