import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = math.inf
        max_price = 0

        for idx in range(len(prices)):
            if prices[idx] < min_price:
                min_price = prices[idx]
            elif prices[idx] - min_price > max_price:
                max_price = prices[idx] - min_price

        return max_price