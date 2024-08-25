# 풀이
- LeetCode 75, Medium
- Hash Map / Set
- Time: 15m?
- 처음에 생각했던 방법이 아니어서 약간 수정을 하긴 했는데 어렵진 않았음

## 내 풀이
```py
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        height_list = [] # 세로 목록 저장
        cnt = 0
        for i in range(n):

            height = []
            for j in range(n):
                height.append(grid[j][i])
            height_list.append(height)

        for i in range(n):
            for j in range(n):
                if height_list[i] == grid[j]:  # 세로랑 가로랑 비교해서 같으면 cnt += 1
                    cnt += 1
        return cnt
```

## 다른 풀이
### Approach 1: Brute Force
삼중포문으로 해결하는 방법
```py
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0  # 행과 열이 동일한 경우의 수를 저장할 변수
        n = len(grid)  # grid의 크기
        
        # 각 행 r과 각 열 c를 비교합니다.
        for r in range(n):
            for c in range(n):
                match = True  # 초기에는 행과 열이 동일하다고 가정
                
                # 행 r과 열 c를 비교합니다.
                for i in range(n):
                    if grid[r][i] != grid[i][c]:  # 행과 열의 원소가 다르면 match를 False로 설정
                        match = False
                        break
                        
                # 행 r과 열 c가 동일하면 count를 1 증가
                count += int(match)
                    
        return count  # 동일한 경우의 수를 반환
```

### Approach 2: Hash Map
튜플을 사용해서 행(가로)의 빈도수를 계산하고, 열(세로)와 동일한 경우의 수를 누적해서 리턴.
```py
from collections import Counter
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0  # 행과 열이 동일한 경우의 수를 저장할 변수
        n = len(grid)  # grid의 크기
        
        # 각 행을 튜플로 변환하여 빈도 수를 기록합니다.
        row_counter = Counter(tuple(row) for row in grid)

        # 각 열을 튜플로 변환하고, 행 빈도 수와 비교하여 동일한 경우의 수를 누적합니다.
        for c in range(n):
            col = [grid[i][c] for i in range(n)]  # 열 c의 모든 원소를 추출하여 리스트로 만듭니다.
            count += row_counter[tuple(col)]  # 열을 튜플로 변환하고 빈도 수를 확인하여 누적합니다.

        return count  # 동일한 경우의 수를 반환
```

### Approach 3: Trie
트리로 해결할 수도 있다고 한다. 트리로는 문제를 잘 안풀어봐서 생소하다.
```py
from typing import List

class TrieNode:
    def __init__(self):
        self.count = 0  # 이 노드를 끝으로 하는 리스트의 빈도 수
        self.children = {}  # 자식 노드를 저장하는 딕셔너리

class Trie:
    def __init__(self):
        self.trie = TrieNode()  # Trie의 루트 노드

    def insert(self, array: List[int]) -> None:
        my_trie = self.trie
        for a in array:
            if a not in my_trie.children:
                my_trie.children[a] = TrieNode()  # 자식 노드가 없으면 생성
            my_trie = my_trie.children[a]  # 현재 노드를 자식 노드로 이동
        my_trie.count += 1  # 리스트의 빈도 수 증가

    def search(self, array: List[int]) -> int:
        my_trie = self.trie
        for a in array:
            if a in my_trie.children:
                my_trie = my_trie.children[a]  # 자식 노드로 이동
            else:
                return 0  # 해당 리스트가 Trie에 없으면 0 반환
        return my_trie.count  # 리스트의 빈도 수 반환

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        my_trie = Trie()
        count = 0  # 동일한 행과 열의 수를 저장할 변수
        n = len(grid)  # grid의 크기
        
        for row in grid:
            my_trie.insert(row)  # 각 행을 Trie에 삽입
        
        for c in range(n):
            col_array = [grid[i][c] for i in range(n)]  # 열을 리스트로 변환
            count += my_trie.search(col_array)  # 열이 Trie에 몇 번 존재하는지 검색하여 누적
        
        return count  # 결과 반환

```