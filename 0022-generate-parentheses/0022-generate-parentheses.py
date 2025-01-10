class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def backTracking(curr: List[str], left_count, right_count):
            if len(curr) == n * 2:  # 길이 다 채운 경우
                answer.append("".join(curr))
                return

            if left_count < n:  # 왼쪽 덜 채운 경우
                curr.append("(")  # 왼쪽 추가하고
                backTracking(curr, left_count + 1, right_count)
                curr.pop()

            if right_count < left_count:  # 오른쪽 덜 채운 경우
                curr.append(")")  # 오른쪽 추가하고
                backTracking(curr, left_count, right_count + 1)  # 다음으로 넘어가기
                curr.pop()

        backTracking([], 0, 0)
        return answer