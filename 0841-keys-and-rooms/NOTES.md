# 풀이
- LeetCode 75, Medium
- Graphs - DFS
- Time: 10m? (시간 측정 까먹음)
- 오랜만에 DFS 문제 풀어서 처음에 약간 버벅했는데 금방 품

## 내 풀이
```py
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = []
        q.extend(rooms[0])

        visited_room = [0] * len(rooms)
        visited_room[0] = 1  # 첫번째 방은 방문함

        while q:
            key = q.pop()  # 내가 보유한 열쇠
            if visited_room[key] == 0:  # 방문한 적 없으면
                q.extend(rooms[key])  # 해당 방에 있는 열쇠 다 q에 넣기
                visited_room[key] = 1  # 방문처리
    
        if sum(visited_room) == len(rooms):  # 다 방문했으면
            return True
        return False
```

## 다른 풀이
### Approach #1: Depth-First Search [Accepted]
나랑 코드 비슷함. 나는 all 이라는 내장함수 있는줄 모르고 숫자로 처리했음.
```py
class Solution(object):
    def canVisitAllRooms(self, rooms):
        # 모든 방이 방문되었는지 추적하기 위해 'seen' 리스트를 사용
        seen = [False] * len(rooms)  # 모든 방을 처음에는 방문하지 않은 상태로 설정
        seen[0] = True  # 0번 방은 처음에 열려 있으므로 방문 처리
        stack = [0]  # 방문할 방의 키를 저장하는 스택에 0번 방의 키를 추가

        # 처음에 우리는 사용해야 할 키들의 'stack'이 있습니다.
        # 'seen' 리스트는 우리가 이 방에 들어간 적이 있는지 나타냅니다.
        while stack:  # 사용할 키가 남아 있는 동안...
            node = stack.pop()  # 다음 키 'node'를 가져옴
            for nei in rooms[node]:  # 방 'node'에 있는 모든 키에 대해...
                if not seen[nei]:  # 아직 사용되지 않은 키라면
                    seen[nei] = True  # 그 방에 들어갔다고 표시
                    stack.append(nei)  # 할 일 목록에 키를 추가
        return all(seen)  # 모든 방을 방문한 경우에만 True를 반환

```


### Approach 2:
```py
```

### Approach 3:
```py
```