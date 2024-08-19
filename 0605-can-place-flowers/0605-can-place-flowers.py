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