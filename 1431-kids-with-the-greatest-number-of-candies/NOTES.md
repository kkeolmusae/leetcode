# 풀이
- LeetCode 75, Easy
- Array / String
- Time: 5m
- 쉽게 풀었음

## 내 풀이
```py
​from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)  # 제일 많은 캔디를 가진 애를 찾아서

        result = []
        for candy in candies:
            if candy + extraCandies >= max_num:  # 캔디 + 여유 캔디 >= 최대캔디  이면 조건이 맞고
                result.append(True)
            else:  # 아니면 틀린거
                result.append(False)
        return result
```