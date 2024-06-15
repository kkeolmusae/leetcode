from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix[0]) # 세로
        width = len(matrix) # 가로
    
        memory = set()
        
        start, end = 0, 0
        result = []
        
        direction = 0
        d = [
            [0, 1], # 동
            [1, 0], # 남
            [0, -1], # 서
            [-1, 0], # 북 
        ]
        
        while len(result) != height * width:
            result.append(matrix[start][end])
            memory.add((start, end))
            
            nx, ny = start + d[direction][0], end + d[direction][1]
            if (nx,ny) in memory or nx <0 or ny< 0 or nx >= width or ny >= height: # 방문한적 있거나 배열 범위 벗어나면 방향 전환
                direction = (direction + 1) % 4
                nx, ny = start + d[direction][0], end + d[direction][1]
            start, end = nx, ny
        
        return result