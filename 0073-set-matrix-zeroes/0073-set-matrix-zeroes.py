class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        garo = len(matrix[0])
        sero = len(matrix)

        zero = set()  # 0 위치 저장
        for i in range(sero):
            for j in range(garo):
                if matrix[i][j] == 0:
                    zero.add((i, j))

        for i, j in zero:
            for x in range(garo):  # 가로줄 0처리
                matrix[i][x] = 0
            for x in range(sero):  # 세로줄 0처리
                matrix[x][j] = 0
