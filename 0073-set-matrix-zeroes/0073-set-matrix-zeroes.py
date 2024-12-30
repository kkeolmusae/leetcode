class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        width = len(matrix[0])
        height = len(matrix)

        zero = set()
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    zero.add((i, j))

        for i, j in zero:
            for idx in range(height):
                matrix[idx][j] = 0
            for idx in range(width):
                matrix[i][idx] = 0