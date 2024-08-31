class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)  # 도시수
        cnt = 0

        q = deque()
        isChecked = [False] * n

        def dfs(q, isChecked):
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
                dfs(q, isChecked)
                cnt += 1  # 다 처리했으면 cnt += 1
        return cnt
