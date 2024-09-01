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