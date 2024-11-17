class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)  # 행 길이 계산
        m = len(matrix[0])  # 열 길이 계산
        temp = copy.deepcopy(matrix)
        for i in range(n):
            for j in range(m):
                matrix[j][n - i - 1] = temp[i][j]