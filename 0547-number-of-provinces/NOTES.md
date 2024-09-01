# 풀이
- LeetCode 75, Medium
- Graphs - DFS
- Time: 7m 18s?
- Union Find로 풀려고 했는데 기억이 안나서 BFS 로 품. 어렵진않았는데 유형이 익숙치 않았음

## 내 풀이
```py
class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)  # 도시수
        cnt = 0

        q = deque()
        isChecked = [False] * n

        def bfs(q, isChecked):
            while q:
                connected_cities = q.popleft()  # 도시와 연결되어 있는 도시들 꺼내서
                for city_idx in range(len(connected_cities)):
                    # 처리한적 없고 연결되어있으면
                    if connected_cities[city_idx] == 1 and not isChecked[city_idx]:
                        q.append(isConnected[city_idx])
                        isChecked[city_idx] = True

        for idx in range(n):
            if not isChecked[idx]:  # 처리한 적없으면
                isChecked[idx] = True
                q.append(isConnected[idx])  # 해당 도시와 연결되어있는 도시들 집어 넣고
                bfs(q, isChecked)
                cnt += 1  # 다 처리했으면 cnt += 1
        return cnt
```

## 다른 풀이
### Approach 1: Depth First Search
```py
class Solution:
    def dfs(self, node, isConnected, visit):
        visit[node] = True
        for i in range(len(isConnected)):
            if isConnected[node][i] == 1 and not visit[i]:
                self.dfs(i, isConnected, visit)

    def findCircleNum(self, isConnected):
        n = len(isConnected)
        numberOfComponents = 0
        visit = [False] * n

        for i in range(n):
            if not visit[i]:
                numberOfComponents += 1
                self.dfs(i, isConnected, visit)

        return numberOfComponents

```

### Approach 2: Breadth First Search
```py
from collections import deque

class Solution:
    def bfs(self, node, isConnected, visit):
        q = deque([node])
        visit[node] = True

        while q:
            node = q.popleft()

            for i in range(len(isConnected)):
                if isConnected[node][i] == 1 and not visit[i]:
                    q.append(i)
                    visit[i] = True

    def findCircleNum(self, isConnected):
        n = len(isConnected)
        numberOfComponents = 0
        visit = [False] * n

        for i in range(n):
            if not visit[i]:
                numberOfComponents += 1
                self.bfs(i, isConnected, visit)

        return numberOfComponents

```

### Approach 3: Union-find

```py
class UnionFind:
    def __init__(self, size):
        # 초기화: 각 노드는 자기 자신을 부모로 가짐
        self.parent = list(range(size))
        # 각 노드의 rank는 0으로 초기화
        self.rank = [0] * size

    def find(self, x):
        # 경로 압축 최적화: 부모가 자신이 아니라면 재귀적으로 부모를 찾음
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_set(self, x, y):
        # x와 y의 집합을 합침 (union)
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        # rank를 비교하여 작은 쪽을 큰 쪽에 붙임
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1

class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        dsu = UnionFind(n)
        numberOfComponents = n

        # 각 도시 쌍을 비교하여 연결된 도시를 Union-Find로 합침
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1 and dsu.find(i) != dsu.find(j):
                    numberOfComponents -= 1
                    dsu.union_set(i, j)

        return numberOfComponents

```