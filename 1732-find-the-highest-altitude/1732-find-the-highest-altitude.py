from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        start = 0
        for num in gain:
            start += num
            result = max(result, start)
        return result