# 풀이
- Difficulty:  Medium
- Topic:  Graphs
- Elapsed Time:  1m
- Status:  O
- Memo: 이걸 DFS/BFS 로 풀어야하는 이유를 몰라서 그냥 쉽게 풀었다

## 내 풀이
그냥 deepcopy한 결과를 리턴했다. 
```py
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return copy.deepcopy(node)
```

## 다른 풀이
### Approach 1: Depth First Search
출제 의도는 아마 DFS/BFS 로 입력받은 그래프와 똑같은 그래프를 만들어내라는 것이었나보다
```py
class Solution:

    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        clone_node = Node(node.val, [])

        self.visited[node] = clone_node

        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node
```

### Approach 2: Breadth First Search
```py
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque


class Solution:

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:

        if not node:
            return node

        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val, [])


        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]
```