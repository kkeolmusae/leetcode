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