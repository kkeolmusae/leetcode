# 풀이
- LeetCode 75, Medium
- Backtracking
- Time: 3m? 
- 걍 combinations 쓰면 한방에 해결될 것 같았음.

## 내 풀이
```py
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > n:
            return []

        l = list(combinations(list(range(1, 10)), k))

        result = []
        for nums in l:
            if sum(nums) == n:
                result.append(list(nums))
        return result
```

## 다른 풀이
### Approach: Backtracking
백트래킹으로 풀면 이렇다고 한다.
```py
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []  # 결과를 저장할 리스트

        # 백트래킹 함수: 남은 값, 현재 조합, 다음 숫자의 시작 위치
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                # 남은 값이 0이고, 조합의 길이가 k이면 유효한 조합이므로 결과에 추가
                results.append(list(comb))  # 현재 조합을 복사하여 저장
                return
            elif remain < 0 or len(comb) == k:
                # 남은 값이 0보다 작거나, 조합의 길이가 k 이상이면 더 이상 탐색하지 않음
                return

            # 다음 숫자들을 순차적으로 선택하여 백트래킹
            for i in range(next_start, 9):
                comb.append(i + 1)  # 숫자 추가 (1부터 9까지)
                backtrack(remain - i - 1, comb, i + 1)  # 남은 값 업데이트 후 재귀 호출
                comb.pop()  # 백트래킹: 현재 선택을 되돌림

        # 초기 호출: n은 목표 값, 빈 조합, 0부터 시작
        backtrack(n, [], 0)

        return results  # 가능한 모든 조합 반환
```