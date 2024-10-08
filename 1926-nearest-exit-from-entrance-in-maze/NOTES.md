# 풀이
- LeetCode 75, Medium
- Graphs - BFS
- Time: 15m?
- 오랜만에 풀었는데 생각보다 금방 품. 

## 내 풀이
처음에 checked 를 for 문 내에서 해서 Time Limit이 발생했었고, checked 를 for문 돌기 전에 확인하게 함으로서 문제 해결함
```py
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        garo = len(maze[0])
        sero = len(maze)

        q = deque()
        dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오 아 왼 위 방향으로 회전
        checked = defaultdict(bool)

        q.append(entrance + [0])

        while q:
            cx, cy, cnt = q.popleft()  # current x, y
            if checked[(cx, cy)]:  # 방문했던 곳이면 패스 (Time Limit 방지)
                continue
            for dx, dy in dxdy:
                nx = cx + dx
                ny = cy + dy

                # 범위 내에 있으면
                if nx >= 0 and nx < sero and ny >= 0 and ny < garo:
                    # 막다른 벽이 아니면
                    if maze[nx][ny] != "+":
                        q.append([nx, ny, cnt + 1])
                elif cnt != 0:  # 이동은 무조건 해야해
                    return cnt
            checked[(cx, cy)] = True
        return -1

```

## 다른 풀이
### Approach 1: Breadth First Search (BFS)
거의 내 코드랑 비슷한듯 
```py
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # 미로의 행과 열 크기를 변수에 저장
        rows, cols = len(maze), len(maze[0])
        
        # 상하좌우 방향을 나타내는 좌표 변화 (dir)
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        # 입구 좌표를 받아와 시작 좌표로 설정하고, 입구를 방문한 것으로 표시(출구가 아니므로)
        start_row, start_col = entrance
        maze[start_row][start_col] = "+"
        
        # 입구에서 BFS 탐색을 시작하기 위해 큐(queue)를 생성하고, 현재 위치와 거리를 저장
        queue = collections.deque()
        queue.append([start_row, start_col, 0])
        
        # 큐가 빌 때까지 BFS 탐색을 진행
        while queue:
            # 큐에서 현재 위치와 거리를 꺼냄
            curr_row, curr_col, curr_distance = queue.popleft()
            
            # 현재 위치의 네 방향에 대해 탐색
            for d in dirs:
                next_row = curr_row + d[0]
                next_col = curr_col + d[1]
                
                # 방문하지 않은 빈 공간이 있는 경우
                if 0 <= next_row < rows and 0 <= next_col < cols \
                    and maze[next_row][next_col] == ".":
                    
                    # 빈 공간이 출구일 경우, 현재 거리 + 1을 반환
                    if 0 == next_row or next_row == rows - 1 or 0 == next_col or next_col == cols - 1:
                        return curr_distance + 1
                    
                    # 출구가 아닌 경우, 해당 위치를 큐에 추가하고 방문한 것으로 표시
                    maze[next_row][next_col] = "+"
                    queue.append([next_row, next_col, curr_distance + 1])
            
        # 출구를 찾지 못하고 반복이 종료되면 -1을 반환
        return -1

```