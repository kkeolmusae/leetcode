class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:

        graph = defaultdict(defaultdict)

        for idx in range(len(equations)):  # 그래프 초기화
            x, y = equations[idx]
            graph[x][y] = values[idx]
            graph[y][x] = 1 / values[idx]

        def dfs(curr, y, result, checked):
            checked.add(curr)  # 현재 노드 방문 처리
            neighbors = graph[curr]  # 현재 노드랑 인접한 노드들
            ret = -1.0

            if y in neighbors:  # 최종 목적지 y가 현재 노드랑 인접해있으면
                ret = result * neighbors[y]  # ret 갱신
            else:  # curr -> y 가 없으면 (못찾음)
                for next, value in neighbors.items():  # 현재 노드랑 인접한 노드들
                    if next in checked:  # 인접한 노드들중 방문한적 있는 노드면
                        continue

                    # 방문한적없으면 (인접한 노드 -> y) 의 길이 있는지 체크
                    ret = dfs(next, y, value * result, checked)

                    if ret != -1.0:  # y에 도달했으면 ret이 -1.0이 아님
                        break

            checked.remove(curr)
            return ret

        result = []
        ret = 0
        for x, y in queries:
            if x not in graph or y not in graph:  # 없는 값일때
                ret = -1.0
            elif x == y:
                ret = 1.0
            else:
                checked = set()
                ret = dfs(x, y, 1, checked)
            result.append(ret)

        return result