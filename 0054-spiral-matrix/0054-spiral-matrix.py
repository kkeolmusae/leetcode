class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        checked = math.inf
        height = len(matrix)  # 세로
        width = len(matrix[0])  # 가로

        total = height * width  # 전체 숫자 개수
        x, y = 0, 0

        direction = 0  # 방향
        dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오 아 왼 위 방향으로 회전

        while total:
            result.append(matrix[x][y])  # 숫자 저장
            matrix[x][y] = checked  # 방문 처리
            total -= 1  # 전체 개수 감소
            nx, ny = x + dxdy[direction][0], y + dxdy[direction][1]  # 다음 좌표

            # 회전해야하는 경우
            if (
                nx >= height
                or nx < 0
                or ny < 0
                or ny >= width
                or matrix[nx][ny] == checked
            ):
                direction = (direction + 1) % 4
                nx, ny = x + dxdy[direction][0], y + dxdy[direction][1]
            x, y = nx, ny
        return result
