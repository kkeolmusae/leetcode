# 풀이
- Difficulty:  Medium
- Topic:  Array / String
- Elapsed Time:  15m
- Status:  O (2 times)
- Memo: 이전에 O(n^2)으로 풀었던 건데 이번에는 O(n) 으로 품

## 내 풀이
```py
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1 or nums[0] == 0:
            return 0

        curr = 0  # 현재 위치
        can_jump = 0  # 현재 위치에서 점프 가능한 최대 위치
        can_jump_max = 0  # 최대 점프 가능한 위치
        last_idx = len(nums) - 1  # 마지막 위치
        answer = 0

        while curr < last_idx:
            # 최대 점프 가능한 위치는 지속적으로 갱신
            can_jump_max = max(curr + nums[curr], can_jump_max)

            # 현재 위치에서 점프 가능한 최대 위치에 도달하면
            if curr == can_jump:
                answer += 1  # 점프 횟수 증가
                can_jump = can_jump_max  # 현재 위치에서 점프 가능한 최대 위치 갱신
            curr += 1  # 다음 발판으로
        return answer

```

## 다른 풀이
### Approach 1: Greedy
```py
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 초기화: 점프 횟수(answer), 배열 길이(n)
        answer, n = 0, len(nums)
        # 현재 점프가 도달할 수 있는 최대 범위(cur_end), 현재 점프 내에서 도달 가능한 최대 위치(cur_far)
        cur_end, cur_far = 0, 0

        # 마지막 위치는 목표이므로 n - 1까지만 탐색
        for i in range(n - 1):
            # 현재 위치에서 도달 가능한 가장 먼 위치 갱신
            cur_far = max(cur_far, i + nums[i])

            # 현재 점프의 범위가 끝나는 시점
            if i == cur_end:
                # 점프 횟수 증가
                answer += 1
                # 다음 점프의 범위를 갱신
                cur_end = cur_far

        # 최소 점프 횟수 반환
        return answer

```