# 풀이
- LeetCode 75, Medium
- Binary Search
- Time: x 
- 브루트포스 외에 다른 방법이 생각이 도무지 안나서 해설보고 이해하고 품

## 내 풀이
해설보고 이해하고 다시 푼거라 Approach2 랑 크게 다르지 않음 
```py
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles 길이 == h 이면 걍 piles중 최대값을 리턴하면 됨
        if len(piles) == h:  
            return max(piles)

        # 최소 스피드랑 최대 스피드.
        min_speed = 1  # 시간당 1개
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
```

## 다른 풀이
### Approach 1: Brute Force

```py
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 처음 먹는 속도를 1로 설정
        speed = 1

        while True:
            # hour_spent는 현재 속도에서 코코가 총 몇 시간을 소비했는지를 나타냄
            hour_spent = 0

            # 각 바나나 더미에서 소비되는 시간을 계산하여 hour_spent에 더함
            # ceil(pile / speed) 방식으로 시간 계산 (한 시간에 speed 개씩 먹기)
            for pile in piles:
                hour_spent += math.ceil(pile / speed)    

            # 만약 코코가 h 시간 내에 바나나를 다 먹을 수 있으면, 해당 속도 반환
            # 그렇지 않으면, 속도를 1씩 증가시키고 다시 계산
            if hour_spent <= h:
                return speed
            else:
                speed += 1

```

### Approach 2: Binary Search
```py
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        # 먹는 속도의 왼쪽 경계와 오른쪽 경계를 초기화
        left = 1
        right = max(piles)
        
        while left < right:
            # 왼쪽과 오른쪽 경계의 중간값 계산
            # hour_spent는 코코가 총 몇 시간을 소비했는지를 나타냄
            middle = (left + right) // 2            
            hour_spent = 0
            
            # 각 더미에서 걸리는 시간을 계산하여 hour_spent에 더함
            # ceil(pile / middle) 방식으로 시간 계산 (한 시간에 middle 개씩 먹기)
            for pile in piles:
                hour_spent += math.ceil(pile / middle)
            
            # 중간값 속도가 가능한지 확인하고, 탐색 범위를 반으로 줄임
            if hour_spent <= h:
                right = middle
            else:
                left = middle + 1
        
        # 왼쪽과 오른쪽 경계가 같아지면 최소 먹는 속도를 찾음
        return right
```