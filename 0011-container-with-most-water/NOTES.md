# 풀이
- LeetCode 75, Medium
- Two Pointers
- Time: 4m 20s
- 지난번에 풀었던 문제인데 그냥 다시 풀어봄.

## 내 코드
1. 좌우에서 한칸씩 중앙으로 당기면서 최대 너비를 갱신하고,
2. (왼쪽 길이 < 오른쪽 길이) 이면 왼쪽을 오른쪽으로 이동하고, 
3. (오른쪽 길이 < 왼쪽 길이) 이면 오른쪽을 왼쪽으로 이동하는 방식으로 움직이면서 최대값을 구함
```py
class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        l_idx = 0
        r_idx = len(height) - 1

        while l_idx < r_idx:
            w = r_idx - l_idx  # 가로
            h = min(height[l_idx], height[r_idx])  # 세로
            result = max(result, w * h)  # 최대 넓이 갱신

            if height[l_idx] < height[r_idx]:  # 왼쪽이 짧으면 왼쪽꺼 이동해보기
                l_idx += 1
            else:  # 아니면 오른쪽꺼 이동
                r_idx -= 1

        return result
```

## 다른 풀이
### Brute Force
```py
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        for left in range(len(height)): # 왼쪽을 기준으로
            for right in range(left + 1, len(height)): #
                width = right - left
                maxarea = max(maxarea, min(height[left], height[right]) * width)

        return maxarea
```

### Two Pointer
내 풀이랑 비슷함
```py
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return maxarea
```

