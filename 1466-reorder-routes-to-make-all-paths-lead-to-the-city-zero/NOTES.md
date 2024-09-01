# 풀이
- LeetCode 75, Medium
- Graphs - DFS
- Time: 21m
- 처음 코드는 시간초과 발생했었음. 그래프 문제를 좀 풀어야 할 것 같은 느낌..

## 내 풀이

### 처음 코드 (시간초과)
모든 연결 방향 및 유무를 저장했는데 이거때문에 시간초과 발생한듯
```py
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        directions = [[0 for _ in range(n)] for _ in range(n)]
        cnt = 0  # 변경 횟수

        checked = [False] * n  # 확인했는지
        for x, y in connections:  # 방향 저장
            directions[x][y] = 1  # x -> y 면 1
            directions[y][x] = -1  # 반대방향도 표기

        q = deque([0])  # 0에서 부터 가까운거 부터

        # 다 체크할 때 까지
        while q:
            curr_node = q.popleft()  # 이 노드로 방향이 되어있어야함

            for node in range(n):
                if checked[node] == True or directions[curr_node][node] == 0:
                    continue
                if directions[curr_node][node] == 1:  # 방향이 반대인 경우
                    cnt += 1
                    directions[curr_node][node] = -1
                    directions[node][curr_node] = 1
                q.append(node)
            checked[curr_node] = True

        return cnt
```

### 개선한 코드
필요한 방향만 저장함
```py
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        directions = defaultdict(list)  # 방향 저장
        cnt = 0  # 변경 횟수

        checked = [False] * n  # 확인했는지
        for x, y in connections:  # 방향 저장
            directions[x].append((y, 1))  # x -> y 면 1
            directions[y].append((x, 0))  # 반대방향은 0으로 저장

        q = deque([0])  # 0에서 부터 가까운거 부터

        # 다 체크할 때 까지
        while q:
            curr_node = q.popleft()  # 이 노드로 방향이 되어있어야함

            for node, direction in directions[curr_node]:
                if checked[node] == True:
                    continue

                if direction:  # 방향 바꿔야하는경우
                    cnt += 1
                q.append(node)
            checked[curr_node] = True

        return cnt
```

## 다른 풀이
### Approach 1: Depth First Search
```py
class Solution:
    def __init__(self):
        self.count = 0  # 방향을 변경한 횟수

    def dfs(self, node, parent, adj):
        # 현재 노드에서 이동할 수 있는 모든 이웃을 탐색
        if node not in adj:
            return
        for neighbor, sign in adj[node]:
            if neighbor != parent:  # 부모 노드가 아닌 경우
                self.count += sign  # 방향이 반대인 경우 1을 더함
                self.dfs(neighbor, node, adj)  # 이웃 노드를 재귀적으로 탐색

    def minReorder(self, n, connections):
        # 인접 리스트 생성
        adj = {}
        for connection in connections:
            # 연결된 노드를 adj에 추가하고, 방향성을 표시
            adj.setdefault(connection[0], []).append([connection[1], 1])  # 0 -> 1 방향
            adj.setdefault(connection[1], []).append([connection[0], 0])  # 1 -> 0 방향 (올바른 방향)

        # DFS를 시작하여 방향이 잘못된 도로의 개수를 세기
        self.dfs(0, -1, adj)
        return self.count

```

### Approach 2: Breadth First Search
```py
from collections import deque

class Solution:
    def __init__(self):
        self.count = 0  # 방향을 변경한 횟수

    def bfs(self, node, n, adj):
        q = deque([node])  # BFS 탐색을 위한 큐
        visit = [False] * n  # 방문 여부를 체크하기 위한 리스트
        visit[node] = True  # 시작 노드 방문 체크

        while q:
            node = q.popleft()  # 현재 노드를 큐에서 꺼냄
            if node not in adj:  # 만약 인접 리스트에 현재 노드가 없다면 넘어감
                continue
            for neighbor, sign in adj[node]:  # 인접 노드와 방향성 탐색
                if not visit[neighbor]:  # 인접 노드가 아직 방문되지 않았다면
                    self.count += sign  # 잘못된 방향(1)이면 count 증가
                    visit[neighbor] = True  # 인접 노드 방문 체크
                    q.append(neighbor)  # 인접 노드를 큐에 추가

    def minReorder(self, n, connections):
        adj = {}  # 인접 리스트를 위한 딕셔너리
        for connection in connections:
            adj.setdefault(connection[0], []).append([connection[1], 1])  # 잘못된 방향
            adj.setdefault(connection[1], []).append([connection[0], 0])  # 올바른 방향

        self.bfs(0, n, adj)  # BFS로 탐색 시작
        return self.count  # 변경된 도로의 수 반환

```