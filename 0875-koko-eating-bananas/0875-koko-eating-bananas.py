class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)

        min_speed = 1
        max_speed = max(piles)

        while min_speed < max_speed:
            mid = (min_speed + max_speed) // 2
            hour_spent = 0

            for pile in piles:
                hour_spent += ceil(pile / mid)  # ceil = 올림

            # 사용한 시간이 h 보다 크면 한번에 먹을 수 있는 바나나가 개수 늘려야함. min_spped를 올리자
            if hour_spent > h:
                min_speed = mid + 1
            elif hour_spent <= h:  # 사용한 시간이 h 보다 작거나 같으면 min_spped 줄이자
                max_speed = mid

        return max_speed