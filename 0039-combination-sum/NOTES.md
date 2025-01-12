# 풀이
- Difficulty: Medium
- Topic:  Backtracking
- Elapsed Time:  12m
- Status:  O
- Memo: 백트래킹에 대한 감이 좀 잡히는듯한데 아직 10문제는 더 풀어봐야할듯하다.

## 내 풀이
```py
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []  # 모든 유효한 조합을 저장할 리스트
        n = len(candidates)  # 후보 숫자 리스트의 길이

        def backtracking(curr: List[int], idx: int):
            if sum(curr) == target:  # 현재 조합의 합이 타겟과 같으면
                result.append(curr[:])  # 결과 리스트에 현재 조합의 복사본 추가
                return

            if sum(curr) > target:  # 현재 조합의 합이 타겟보다 크면
                return  # 더 이상 진행하지 않고 종료

            for i in range(idx, n):
                curr.append(candidates[i])  # 현재 숫자를 조합에 추가
                backtracking(curr, i)  # 같은 숫자를 다시 사용할 수 있으므로 i부터 시작
                curr.pop()  # 백트래킹: 추가했던 숫자 제거

        backtracking([], 0)  # 초기 호출: 빈 리스트, 인덱스 0
        return result  # 모든 유효한 조합 반환
```

## 다른 풀이
### Approach 1: Backtracking
오 내 방식이랑 비슷하다. 꽤나 정석대로 풀었나보다.
```py
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []  # 모든 유효한 조합을 저장할 리스트

        def backtrack(remain, comb, start):
            if remain == 0:
                # 남은 값이 0이면 유효한 조합을 찾은 것
                # 현재 조합의 깊은 복사본을 결과에 추가
                results.append(list(comb))
                return
            elif remain < 0:
                # 남은 값이 음수면 조합의 합이 타겟을 초과한 것
                # 더 이상의 탐색을 중단
                return

            for i in range(start, len(candidates)):
                # 현재 숫자를 조합에 추가
                comb.append(candidates[i])
                # 현재 숫자를 다시 사용할 수 있으므로 인덱스 i부터 재귀 호출
                backtrack(remain - candidates[i], comb, i)
                # 백트래킹: 추가했던 숫자를 제거
                comb.pop()

        backtrack(target, [], 0)  # 초기 호출: 타겟값, 빈 조합, 시작 인덱스 0

        return results  # 모든 유효한 조합 반환
```
