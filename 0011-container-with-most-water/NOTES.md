# 풀이
- Difficulty:  Medium
- Topic:  Two Pointers
- Elapsed Time:  6m
- Status:  O (3 times)
- Memo: 예전에 풀어봤던거라 그런지 별로 안어려웠음.

## 내 풀이
```py
class Solution:
    def maxArea(self, height: List[int]) -> int:
        lidx = 0
        ridx = len(height) - 1
        amount = 0

        while lidx < ridx:
            h = min(height[lidx], height[ridx])  # 둘중 낮은게 높이
            amount = max(h * (ridx - lidx), amount)  # amount 갱신
            
            # 길이 더 짧은거 옮기기
            if height[lidx] < height[ridx]:
                lidx += 1
            else:
                ridx -= 1
        return amount
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

