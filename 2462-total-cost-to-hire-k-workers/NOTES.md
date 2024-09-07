# 풀이
- LeetCode 75, Medium
- Heap / Priority Queue
- Time: 17m 23s (리트코드에서 시간 제대로 측정하고 있나...?)
- 문제 이해도 금방하고 방향도 금방 잡았는데 한두개 예외케이스 처리하느라 시간이 좀 더 걸린듯

## 내 풀이
- heapq를 왼쪽그룹 오른쪽그룹 나눠서 2개를 썻고, 그룹에서 pop할때마다 추가해줌. 
- 그리고 k가 0이 되거나 각 그룹에 새로 할당할 cost가 없으면 남은 두 그룹으로 나머지 처리함
```py
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        l_idx = candidates - 1
        r_idx = len(costs) - candidates
        total_cost = 0

        # 그룹 나누는게 의미 없는 경우 (양 그룹의 길이 >= candidates)
        if l_idx >= r_idx:
            heapq.heapify(costs)
            while k:
                total_cost += heapq.heappop(costs)
                k -= 1
            return total_cost

        left_q = costs[: l_idx + 1]
        heapq.heapify(left_q)  # 왼쪽 그룹

        right_q = costs[r_idx:]
        heapq.heapify(right_q)  # 오른쪽 그룹

        while k > 0 and l_idx < r_idx:
            if len(left_q) < candidates:
                heapq.heappush(left_q, costs[l_idx])
            elif len(right_q) < candidates:
                heapq.heappush(right_q, costs[r_idx])

            # 가장 저렴한 인력이 왼쪽에 있거나 양쪽에 있는 경우
            if left_q[0] <= right_q[0]:
                total_cost += heapq.heappop(left_q)
                l_idx += 1
            else:
                total_cost += heapq.heappop(right_q)
                r_idx -= 1
            k -= 1
            print(total_cost)

        # worker 다 쓴 경우
        if k == 0:
            return total_cost

        # 나머지 처리
        while k:
            if not left_q:  # l그룹 다 쓴 경우
                while right_q and k:
                    total_cost += heapq.heappop(right_q)
                    k -= 1
            elif not right_q:  # r 그룹 다 쓴 경우
                while left_q and k:
                    total_cost += heapq.heappop(left_q)
                    k -= 1
            else:  # l,r 그룹 다 남아있는 경우
                if left_q[0] <= right_q[0]:
                    total_cost += heapq.heappop(left_q)
                else:
                    total_cost += heapq.heappop(right_q)
                k -= 1

        return total_cost
```

## 다른 풀이
### Approach 1: 2 Priority Queues
내 코드랑 똑같이 heapq를 두개썼다. 그 외에 근로자를 그룹에서 처리하는 부분은 조금 더 간결하게 짰다.
```py
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # head_workers는 처음 candidates명의 근로자들을 저장하는 리스트입니다.
        # tail_workers는 마지막 candidates명의 근로자들 중 첫 번째 그룹과 겹치지 않는 근로자들을 저장합니다.
        head_workers = costs[:candidates]
        tail_workers = costs[max(candidates, len(costs) - candidates):]
        
        # 두 리스트를 최소 힙으로 변환합니다.
        heapify(head_workers)
        heapify(tail_workers)
        
        answer = 0  # 총 고용 비용을 저장할 변수입니다.
        next_head, next_tail = candidates, len(costs) - 1 - candidates  # 다음에 선택할 근로자들의 인덱스를 저장합니다.

        for _ in range(k): 
            # tail_workers가 비어있거나 head_workers에서의 최솟값이 tail_workers의 최솟값보다 작거나 같으면
            if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]: 
                answer += heappop(head_workers)  # head_workers에서 최솟값을 꺼내 총 비용에 더합니다.

                # 아직 head와 tail 리스트 밖에 선택하지 않은 근로자가 남아있다면 head_workers를 갱신합니다.
                if next_head <= next_tail: 
                    heappush(head_workers, costs[next_head])  # 다음 head 후보를 head_workers에 추가합니다.
                    next_head += 1
            else: 
                answer += heappop(tail_workers)  # tail_workers에서 최솟값을 꺼내 총 비용에 더합니다.

                # 아직 head와 tail 리스트 밖에 선택하지 않은 근로자가 남아있다면 tail_workers를 갱신합니다.
                if next_head <= next_tail:  
                    heappush(tail_workers, costs[next_tail])  # 다음 tail 후보를 tail_workers에 추가합니다.
                    next_tail -= 1
                    
        return answer  # 최종 총 비용을 반환합니다.

```

### Approach 2: 1 Priority Queue
heapq 를 하나써서 하나의 그룹처럼 처리함
```py
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # 첫 번째 candidates명의 근로자를 섹션 ID 0으로, 
        # 마지막 candidates명의 근로자를 섹션 ID 1로 우선순위 큐(pq)에 추가합니다.
        # 중복되지 않도록 처리합니다.
        pq = []
        for i in range(candidates):
            pq.append((costs[i], 0))  # 앞쪽에서 candidates명의 근로자 추가
        for i in range(max(candidates, len(costs) - candidates), len(costs)):
            pq.append((costs[i], 1))  # 뒤쪽에서 candidates명의 근로자 추가

        # 리스트를 최소 힙으로 변환
        heapify(pq)
        
        answer = 0  # 총 비용을 저장할 변수
        next_head, next_tail = candidates, len(costs) - 1 - candidates  # 다음에 추가할 근로자의 인덱스 설정

        # 남은 근로자가 있을 때만 pq에 새로 추가하며, k명의 근로자를 고용할 때까지 반복합니다.
        for _ in range(k): 
            cur_cost, cur_section_id = heappop(pq)  # 현재 최소 비용과 해당 근로자의 섹션 ID를 꺼냅니다.
            answer += cur_cost  # 현재 근로자의 비용을 총 비용에 더합니다.

            # 고용하지 않은 근로자가 남아있다면 pq에 새로 추가합니다.
            if next_head <= next_tail: 
                if cur_section_id == 0:  # 앞쪽 섹션에서 꺼낸 경우
                    heappush(pq, (costs[next_head], 0))  # 다음 앞쪽 근로자를 추가
                    next_head += 1
                else:  # 뒤쪽 섹션에서 꺼낸 경우
                    heappush(pq, (costs[next_tail], 1))  # 다음 뒤쪽 근로자를 추가
                    next_tail -= 1
        
        # 고용한 근로자의 총 비용을 반환합니다.
        return answer

```