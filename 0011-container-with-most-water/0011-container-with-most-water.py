class Solution:
    def maxArea(self, height: List[int]) -> int:
      result = 0
      l_idx = 0
      r_idx = len(height) - 1
      
      # 좌우에서 
      while l_idx < r_idx:
        result = max(result, (r_idx - l_idx) * min(height[l_idx], height[r_idx]))
        if height[l_idx] < height[r_idx]:
          l_idx += 1
        else: 
          r_idx -= 1
      
      return result