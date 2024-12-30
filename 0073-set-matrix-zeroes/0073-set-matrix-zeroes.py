class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)  # 행의 개수
        cols = len(matrix[0])  # 열의 개수

        zero = set()  # 0의 좌표를 저장할 집합
        for i in range(rows):  # 행 순회
            for j in range(cols):  # 열 순회
                if matrix[i][j] == 0:  # 0인 경우
                    zero.add((i, j))  # 좌표 저장

        for i, j in zero:  # 0의 좌표를 순회
            for idx in range(rows):  # 해당 열을 0으로 설정
                matrix[idx][j] = 0
            for idx in range(cols):  # 해당 행을 0으로 설정
                matrix[i][idx] = 0
