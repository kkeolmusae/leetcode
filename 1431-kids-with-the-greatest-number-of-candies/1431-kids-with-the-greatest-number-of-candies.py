from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)

        result = []
        for candy in candies:
            if candy + extraCandies >= max_num:
                result.append(True)
            else:
                result.append(False)
        return result