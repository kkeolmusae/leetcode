from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(rows):
            check = defaultdict(bool)
            
            for r in rows:
                if r == ".":
                    continue
                
                if r not in check:
                    check[r] = True
                else:
                    return False
            return True
        
        def checkCol(board, idx):
            check = defaultdict(bool)
            
            for row in board:
                col = row[idx]
                if col == ".":
                    continue
                
                if col not in check:
                    check[col] = True
                else:
                    return False
            return True
        
        def check_box(board, x, y):
            dxdy = [(0,0), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1, -1), (-1,0), (-1, 1)]
            
            check = defaultdict(bool)
            for dx, dy in dxdy:
                num = board[dx + x][dy + y]
                if num == ".":
                    continue
                
                if num not in check:
                    check[num] = True
                else:
                    return False
            return True
        
        for idx in range(len(board)):
            if not checkRow(board[idx]):
                return False
        for idx in range(len(board)):
            if not checkCol(board, idx):
                return False
        for x, y in [(1,1), (1,4), (1,7), (4,1), (4,4), (4,7), (7,1), (7,4), (7,7)]:
            if not check_box(board, x, y):
                return False
        return True