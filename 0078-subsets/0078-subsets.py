class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def backtracking(curr: List[int], idx: int):
            # 현재 상태를 결과에 추가 (깊은 복사 사용)
            answer.append(curr[:])

            # idx부터 시작해서 모든 원소를 탐색
            for i in range(idx, len(nums)):
                curr.append(nums[i])  # 현재 원소를 추가
                backtracking(curr, i + 1)  # 다음 단계로 재귀 호출
                curr.pop()  # 백트래킹: 상태 복원

        backtracking([], 0)
        return answer