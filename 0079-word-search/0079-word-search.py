class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우, 하, 좌, 상 방향

        def backtracking(x: int, y: int, idx: int) -> bool:
            if idx == len(word):  # 단어를 모두 찾은 경우
                return True

            # 찾고자 하는 문자가 아니라면 False
            if (
                x < 0
                or x >= len(board)
                or y < 0
                or y >= len(board[0])
                or board[x][y] != word[idx]
            ):
                return False

            # 현재 문자를 사용하고 탐색
            temp = board[x][y]
            board[x][y] = False  # 방문 표시
            for dx, dy in dxdy:
                if backtracking(x + dx, y + dy, idx + 1):
                    return True
            board[x][y] = temp  # 복구
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:  # 시작 문자 찾기
                    if backtracking(i, j, 0):
                        return True
        return False