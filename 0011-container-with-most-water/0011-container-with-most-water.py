from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        l_idx = 0
        r_idx = len(height) - 1

        while l_idx < r_idx:
            w = r_idx - l_idx
            h = min(height[l_idx], height[r_idx])
            result = max(result, w * h)

            if height[l_idx] < height[r_idx]:  # 왼쪽이 짧으면 왼쪽꺼 이동해보기
                l_idx += 1
            else:  # 아니면 오른쪽꺼 이동
                r_idx -= 1

        return result