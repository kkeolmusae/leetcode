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
