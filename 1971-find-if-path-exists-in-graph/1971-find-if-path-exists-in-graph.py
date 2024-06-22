from typing import List
from collections import defaultdict, deque


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        q = deque()
        q.append(source)
        is_check = [False] * n
        
        while q:
            node = q.popleft()
            if is_check[node]:
                continue
            is_check[node] = True
            
            if node == destination:
                return True
            
            for i in graph[node]:
                if not is_check[i]:
                    q.append(i)
        return False