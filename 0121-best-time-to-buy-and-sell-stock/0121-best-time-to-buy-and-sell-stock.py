class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0  # 최대 수익
        min_price = math.inf  # 최소 값

        for p in prices:
            if p < min_price:
                # min_price 보다 더 작은게 나왔으면 min 갱신
                min_price = p
            elif p - min_price > max_profit:
                # 현재 가격 - min_price 가 max_profit 보다 크면, max_profit 갱신
                max_profit = p - min_price
        return max_profit