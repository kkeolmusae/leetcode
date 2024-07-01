### Notes
#### DFS 로 푸는 방법
```python
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Store all edges according to nodes in 'graph'.
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # Start from source node, add it to stack.
        seen = [False] * n
        seen[source] = True
        stack = [source]
        
        while stack:
            curr_node = stack.pop()
            # Add all unvisited neighbors of the current node to stack 
            # and mark them as visited.
            for next_node in graph[curr_node]:
                if next_node == destination:
                    return True
                if not seen[next_node]:
                    seen[next_node] = True
                    stack.append(next_node)
        
        return seen[destination]
```

#### Union Find 로 푸는 방법
```python
class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                root_x, root_y = root_y, root_x
            # Modify the root of the smaller group as the root of the
            # larger group, also increment the size of the larger group.
            self.rank[root_y] += self.rank[root_x]
            self.root[root_x] = root_y

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)

        for a, b in edges:
            uf.union(a, b)

        return uf.find(source) == uf.find(destination)
```