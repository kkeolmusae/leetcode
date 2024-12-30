class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        check = set()
        n = len(matrix[0])  # 가로
        m = len(matrix)  # 세로

        total = n * m  # 전체 숫자 개수
        x, y = 0, 0

        direction = 0  # 방향 (처음에는 dxdy[0] 오른쪽)
        dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오 아 왼 위 방향으로 회전

        while total:
            result.append(matrix[x][y])  # 숫자 저장
            total -= 1
            check.add((x, y))
            nx, ny = x + dxdy[direction % 4][0], y + dxdy[direction % 4][1]
            if nx >= m or nx < 0 or ny < 0 or ny >= n or (nx, ny) in check:
                direction += 1
                nx, ny = x + dxdy[direction % 4][0], y + dxdy[direction % 4][1]
            x, y = nx, ny
        return result
