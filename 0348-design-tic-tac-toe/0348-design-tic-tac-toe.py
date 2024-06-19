class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.horiz = [0] * n # 가로 == row
        self.vert = [0] * n # 새로 == col
        self.diag1 = 0 # 왼쪽 위에서 오른쪽 아래로 대각선 
        self.diag2 = 0 # 오른쪽 위에서 왼쪽 아래로 대각선
        

    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        
        # player가 1이면 move = 1. player가 2면 move = -1
        move = 1 if player == 1 else -1
        
        self.horiz[row] += move # 가로에 값 추가
        self.vert[col] += move # 세로에 값 추가
        
        if row == col:
            self.diag1 += move
        
        if row + col == n - 1:
            self.diag2 += move
            
        if abs(self.horiz[row]) == n or abs(self.vert[col]) == n or abs(self.diag1) == n or abs(self.diag2) == n:
            return player

        return 0