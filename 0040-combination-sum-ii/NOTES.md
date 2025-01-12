# 풀이
- Difficulty:  Medium
- Topic:  Backtracking
- Elapsed Time:  24m
- Status:  O 
- Memo:  백트래킹이 어느정도 감이 잡힐랑 말랑하는중이다...

## 내 풀이
- [1,1,1,1,.....,1] 처럼 같은 숫자가 무수히 반복되는 경우 TLE 가 발생하는걸 개선하다가 시간이 오래 걸렸다.
- mem을 사용하여 중복된 배열을 넘어가려 했으나 이 방법으로는 같은 숫자가 반복될때 TLE가 발생했다.
- `i > currIdx and candidates[i] == candidates[i - 1]:` 로 **현재 반복이 반복 단계 내에서 두 번째 이상의 동일 숫자를 처리 중** 이고 **현재 숫자가 이전 숫자와 같음** 인 경우 넘어가게 했다.

```py
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        result = []

        def backtracking(curr: List[int], currIdx: int):
            s = sum(curr)
            if s > target:  # 종료
                return
            elif s == target:
                result.append(curr[:])
                return

            for i in range(currIdx, n):
                # 같은 숫자를 반복적으로 사용하는 경우를 방지
                if i > currIdx and candidates[i] == candidates[i - 1]:
                    continue
                curr.append(candidates[i])
                backtracking(curr, i + 1)
                curr.pop()

            return

        backtracking([], 0)
        return result
```

## 다른 풀이
### Approach: Backtracking
```py
class Solution:
    def combinationSum2(self, candidates, target):
        answer = []  # 모든 유효한 조합을 저장할 리스트
        candidates.sort()  # 중복 제거를 위해 후보 리스트 정렬
        self.backtrack(candidates, target, 0, [], answer)
        return answer

    def backtrack(self, candidates, target, totalIdx, path, answer):
        if target < 0:
            return  # 타겟이 음수면 백트래킹
        if target == 0:
            answer.append(path)
            return  # 타겟이 0이면 유효한 조합을 찾은 것이므로 종료

        for i in range(totalIdx, len(candidates)):
            if i > totalIdx and candidates[i] == candidates[i - 1]:
                continue  # 중복된 조합을 피하기 위해 같은 값의 연속된 원소 건너뛰기
            self.backtrack(
                candidates,
                target - candidates[i],  # 현재 값을 뺀 새로운 타겟
                i + 1,  # 다음 인덱스부터 시작 (각 숫자는 한 번만 사용)
                path + [candidates[i]],  # 현재 값을 경로에 추가
                answer,
            )
```