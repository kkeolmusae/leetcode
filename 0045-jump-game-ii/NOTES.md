### 다른 풀이
일단 내 코드는 O(n^2) 임. dp(?) 처럼 풀었는데 solution 보니깐 O(n)으로 잘 풀었더라. 


```py
class Solution:
    def jump(self, nums: List[int]) -> int:
        # The starting range of the first jump is [0, 0]
        answer, n = 0, len(nums)
        cur_end, cur_far = 0, 0

        for i in range(n - 1):
            # i 위치에서 가장 멀리 갈 수 있는 위치
            cur_far = max(cur_far, i + nums[i])

            # 현재 인덱스 i가 현재 점프에서 도달할 수 있는 최대 인덱스 cur_end에 도달하면, 점프를 완료한 것으로 간주
            # 다음 점프의 최대 도달 가능 인덱스를 현재 점프에서 계산한 최대 인덱스 cur_far로 업데이트
            if i == cur_end:
                answer += 1
                cur_end = cur_far

        return answer
```