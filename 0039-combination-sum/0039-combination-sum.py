class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)

        def backtracking(curr: List[int], idx: int, start: int):
            if sum(curr) == target:  # 타겟과 같으면 result에 더하기
                result.append(curr[:])
                return

            if sum(curr) > target:  # 타겟보다 크면 종료
                return

            for i in range(start, n):
                curr.append(candidates[i])  # 숫자 더하기
                backtracking(curr, idx, i)
                curr.pop()

        backtracking([], 0, 0)
        return result