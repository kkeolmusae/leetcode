class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        result = []
        mem = set()

        def backtracking(curr: List[int], currIdx: int):
            s = sum(curr)
            if s > target or str(curr) in mem:  # 종료
                return
            elif s == target and str(curr) not in mem:
                result.append(curr[:])
                mem.add(str(curr))
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