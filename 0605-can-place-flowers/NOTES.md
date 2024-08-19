# 풀이

- LeetCode 75, Easy
- Time: 11m
- 문제 자체는 굉장히 쉬웠는데 예외처리하느라 시간 좀 더 걸린듯

## 내 풀이
```py
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # 하나만 있는 경우
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            flowerbed[0] = 1
            n -= 1

        # 첫번쨰
        if len(flowerbed) > 1 and flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1

        for idx in range(1, len(flowerbed) - 1):
            bed = flowerbed[idx]
            if bed == 1:
                continue
            else:
                if flowerbed[idx - 1] == 0 and flowerbed[idx + 1] == 0:
                    flowerbed[idx] = 1
                    n -= 1

        # 마지막 처리
        if len(flowerbed) > 1 and flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1

        if n < 1:
            return True
        return False
```

## 다른 풀이

### Approach #1 Single Scan + Optimized [Accepted]
- empty_left_plot: 왼쪽 자리가 비어있는지를 확인. i == 0인 경우(배열의 첫 번째 자리) 왼쪽 자리가 없기 때문에 빈 자리로 간주. 그 외의 경우 flowerbed[i - 1]이 0인지 확인
- empty_right_plot: 오른쪽 자리가 비어있는지를 확인. i == len(flowerbed) - 1인 경우(배열의 마지막 자리) 오른쪽 자리가 없기 때문에 빈 자리로 간주. 그 외의 경우 flowerbed[i + 1]이 0인지 확인
```py
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            
            # 빈 자리인지 확인
            if flowerbed[i] == 0:
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # 양쪽다 비면 꽃 심고 카운트 증가. 만약 n 보다 크면 True 리턴
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
                    
        return count >= n
```