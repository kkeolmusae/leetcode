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