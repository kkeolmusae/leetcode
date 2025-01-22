class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        interval = defaultdict(int)

        # 각 Task 별로 개수 저장
        for t in tasks:
            interval[t] += 1

        # 알파벳별로 주기 저장
        q = [-d for d in interval.values()]
        heapq.heapify(q)  # heapq로

        result = 0
        while q:
            cycle = n + 1  # 사이클 수
            stores = []  # 한 사이클에 한번 처리한건 여기 임시로 넣어둠
            task = 0  # 한 사이클에 처리한 일감

            while cycle > 0 and q:
                curr = heapq.heappop(q)  # 하나 꺼내고
                cycle -= 1  # 사이클 숫자 줄이고
                task += 1  # task 1 늘리고
                if curr < -1:  # 숫자 남아있으면 현재숫자 +1 하고 다시 집어 넣기
                    stores.append(curr + 1)

            # 남은 일감들 q에 넣고
            for num in stores:
                heapq.heappush(q, num)

            if not q:  # 일감없으면 처리한 task만큼 증가
                result += task
            else:  # 일감 남아있으면 한 사이클 다 돈거니깐 n+1 만큼 증가
                result += n + 1

        return result