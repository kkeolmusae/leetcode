class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # 스택: 온도가 높은 날을 찾기 위해 인덱스를 저장
        n = len(temperatures)  # 온도 리스트의 길이
        result = [0] * n  # 결과 리스트 초기화 (모든 값을 0으로 설정)

        for idx in range(n):
            # 스택이 비어 있지 않고, 현재 온도가 스택의 마지막 인덱스 온도보다 높은 경우
            while stack and temperatures[stack[-1]] < temperatures[idx]:
                prev_idx = stack.pop()  # 스택에서 인덱스를 꺼냄
                result[prev_idx] = (
                    idx - prev_idx
                )  # 현재 인덱스와 이전 인덱스의 차이를 결과에 저장

            # 현재 인덱스를 스택에 추가
            stack.append(idx)

        # 최종 결과 반환
        return result