# 풀이
- LeetCode 75, Medium
- Graphs - DFS
- Time: x 
- 못품. 대충 그림으로 그렸을때 감은 잡혔는데 해결 못함. 솔루션보고 이해해서 대강 풀긴했는데 내일 다시 풀어봐야함

## 내 풀이
```py
class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:

        graph = defaultdict(defaultdict)

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

        for idx in range(len(equations)):  # 그래프 초기화
            x, y = equations[idx]
            graph[x][y] = values[idx]
            graph[y][x] = 1 / values[idx]

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
```

## 다른 풀이
### Approach 1: Path Search in Graph
내가 참고한 풀이. 
```py
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # 그래프를 기본 딕셔너리 형태로 초기화
        graph = defaultdict(defaultdict)

        def backtrack_evaluate(curr_node, target_node, acc_product, visited):
            # 현재 노드를 방문 처리
            visited.add(curr_node)
            ret = -1.0  # 결과값이 없을 경우 -1.0 반환
            neighbors = graph[curr_node]  # 현재 노드의 이웃들

            # 목표 노드가 이웃에 있는 경우 값을 곱하여 결과 반환
            if target_node in neighbors:
                ret = acc_product * neighbors[target_node]
            else:
                # 이웃 노드들에 대해 DFS 탐색
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue  # 이미 방문한 노드는 건너뜀
                    ret = backtrack_evaluate(
                        neighbor, target_node, acc_product * value, visited)
                    if ret != -1.0:  # 유효한 경로를 찾았으면 반복 종료
                        break

            # 백트래킹을 위해 현재 노드를 방문 해제
            visited.remove(curr_node)
            return ret

        # Step 1). 방정식으로부터 그래프를 생성
        for (dividend, divisor), value in zip(equations, values):
            # 그래프에 노드와 그 사이의 간선을 추가
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value  # 역 방향의 간선도 추가

        # Step 2). 각 쿼리에 대해 백트래킹(DFS)으로 계산 수행
        results = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                # case 1): 둘 중 하나의 노드가 그래프에 없을 경우
                ret = -1.0
            elif dividend == divisor:
                # case 2): 시작과 끝이 같은 노드일 경우
                ret = 1.0
            else:
                # DFS 탐색을 통해 경로를 찾고 값을 계산
                visited = set()  # 방문한 노드들을 추적하기 위한 집합
                ret = backtrack_evaluate(dividend, divisor, 1, visited)
            # 결과를 리스트에 추가
            results.append(ret)

        return results

```

### Approach 2: Union-Find with Weights
```py
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # 각 변수의 그룹 아이디와 그 변수까지의 가중치를 저장하는 딕셔너리
        gid_weight = {}

        # 특정 노드의 그룹 아이디와 그 그룹까지의 가중치를 찾는 함수
        def find(node_id):
            if node_id not in gid_weight:
                # 처음 등장한 노드는 자기 자신이 그룹 아이디가 되고 가중치는 1로 설정
                gid_weight[node_id] = (node_id, 1)
            group_id, node_weight = gid_weight[node_id]

            if group_id != node_id:
                # 그룹 아이디가 다르면 부모 그룹을 찾아서 재귀적으로 갱신
                new_group_id, group_weight = find(group_id)
                # 노드의 그룹과 가중치를 업데이트
                gid_weight[node_id] = (new_group_id, node_weight * group_weight)
            return gid_weight[node_id]

        # 두 노드를 같은 그룹으로 합치는 함수
        def union(dividend, divisor, value):
            # 두 노드의 그룹 아이디와 가중치를 찾음
            dividend_gid, dividend_weight = find(dividend)
            divisor_gid, divisor_weight = find(divisor)
            if dividend_gid != divisor_gid:
                # 그룹 아이디가 다르면 하나의 그룹으로 병합
                # dividend 그룹을 divisor 그룹에 연결하고, 가중치를 갱신
                gid_weight[dividend_gid] = \
                    (divisor_gid, divisor_weight * value / dividend_weight)

        # Step 1). 방정식을 이용해 그룹을 생성
        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)

        results = []
        # Step 2). 각 쿼리에 대해 "find" 함수를 이용해 계산 수행
        for (dividend, divisor) in queries:
            if dividend not in gid_weight or divisor not in gid_weight:
                # case 1). 변수 중 하나가 등장하지 않은 경우
                results.append(-1.0)
            else:
                # 두 변수의 그룹 아이디와 가중치를 찾음
                dividend_gid, dividend_weight = find(dividend)
                divisor_gid, divisor_weight = find(divisor)
                if dividend_gid != divisor_gid:
                    # case 2). 두 변수가 같은 그룹에 속하지 않으면 -1 반환
                    results.append(-1.0)
                else:
                    # case 3). 두 변수가 같은 그룹에 속하면 계산하여 결과 반환
                    results.append(dividend_weight / divisor_weight)
        return results

```
