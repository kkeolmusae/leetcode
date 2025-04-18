# 풀이
- Difficulty:  Medium
- Topic:  Heap / Priority Queue
- Elapsed Time:  30m
- Status:  X
- Memo:  풀긴풀었는데 전에 푼거 보고 풀어서... 다시 풀어봐야할듯

## 내 풀이
```py
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = defaultdict(int)

        for t in tasks:  # 알파벳 별로 개수 넣고
            dic[t] += 1

        q = [-d for d in dic.values()]  # 알파벳별 개수를 -로 바꿔서 (max heap)
        heapq.heapify(q)  # heapq 로 만들기

        time = 0
        while q:
            cycle = n + 1  # 한 사이클 제한
            stores = []
            task = 0  # 한 사이클에 처리한 일감

            while cycle > 0 and q:
                current = -heapq.heappop(q)  # 하나 꺼내서
                if current > 1:  # 다음에 또 처리해야하는거면 stores에 임시로 넣어두고
                    stores.append(-(current - 1))
                cycle -= 1
                task += 1

            for num in stores:  # 다음에 처리해야하는 task들 q에 넣기
                heapq.heappush(q, num)

            if not q:  # 다음에 처리할 task 가 없는 경우 -> 끝난거니깐 이번에 처리한 task 만큼 시간 증가
                time += task
            else: # 다음에 처리할 task 가 있는 경우 -> 아직 안끝난거니깐 사이클만큼 시간 증가
                time += n + 1
        return time
```

## 다른 풀이
### Approach 1: Using Priority Queue / Max Heap
```py
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Build frequency map
        freq = [0] * 26
        for ch in tasks:
            freq[ord(ch) - ord('A')] += 1
        
        # Max heap to store frequencies
        pq = [-f for f in freq if f > 0]
        heapq.heapify(pq)

        time = 0 # 총 시간

        # pq라는 최대 힙에서 작업들을 하나씩 꺼내서 처리한다. 각 사이클은 n + 1 길이만큼의 시간을 가진다. 이는 동일한 작업이 다시 시작되기 전에 최소한 n 만큼의 시간이 지나야 하기 때문이다.
        while pq:
            cycle = n + 1
            store = []
            task_count = 0

            # 사이클 동안 가능한 만큼 작업을 수행하고, 빈도가 남은 작업들은 따로 저장해둔다(store). 만약 빈도가 1보다 크다면 해당 작업을 다시 큐에 추가하기 위해 빈도를 줄여서 저장한다.
            while cycle > 0 and pq:
                current_freq = -heapq.heappop(pq)
                if current_freq > 1:
                    store.append(-(current_freq - 1))
                task_count += 1
                cycle -= 1

            # 남은 일감들 pq에 다시 저장
            for x in store:
                heapq.heappush(pq, x)

            # 각 사이클이 끝나면, 사이클 동안 실제로 처리한 작업 개수(task_count)에 따라 시간을 계산한다. 만약 작업이 남아 있다면 사이클의 전체 길이(n + 1)만큼의 시간을 추가한다. 그렇지 않다면 처리한 작업 수만큼 시간을 추가한다.
            time += task_count if not pq else n + 1
        return time
```

### Approach 2: Filling the Slots and Sorting
```py
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 각 작업의 빈도를 저장할 배열을 생성한다. 
        # 알파벳은 총 26개이므로 크기가 26인 배열을 준비한다.
        freq = [0] * 26
        for task in tasks:
            # 작업의 알파벳에 해당하는 인덱스를 증가시킨다.
            freq[ord(task) - ord('A')] += 1

        # freq 배열을 오름차순으로 정렬한다. 
        # 이렇게 하면 빈도가 높은 작업이 배열의 끝부분에 위치하게 된다.
        freq.sort()

        # 가장 높은 빈도를 가진 작업을 기준으로 계산한다.
        # freq[25]는 가장 높은 빈도를 나타내며, -1을 하는 이유는 작업이 한 번 처리된 후 
        # 남은 빈 슬롯의 개수를 계산하기 위함이다.
        max_freq = freq[25] - 1

        # 가장 빈도가 높은 작업들 사이에 필요한 idle 슬롯 수를 계산한다.
        idle_slots = max_freq * n

        # 빈도가 높은 순서로 작업을 처리하며 idle 슬롯을 채운다.
        for i in range(24, -1, -1):  # 가장 높은 빈도를 제외한 나머지 빈도를 탐색
            # 현재 작업이 차지할 수 있는 idle 슬롯을 빼준다.
            idle_slots -= min(max_freq, freq[i])

        # idle 슬롯이 남아 있다면 이를 전체 작업 수에 더하고,
        # 그렇지 않다면 단순히 작업의 개수만 반환한다.
        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)

```

### Approach 3: Greedy Approach
- 가장 빈도가 높은 작업을 기준으로 작업 사이에 들어가는 슬롯의 개수와 길이를 계산.
- 나머지 작업들로 빈 슬롯을 채우고, 부족한 부분은 대기시간으로 채움.
- 최종적으로 총 작업 수와 추가 대기 시간을 합산하여 최소 시간을 구함.
```py
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counter = [0] * 26
        max_val = 0 # 가장 빈도수 높은 경우
        max_count = 0 # 가장 빈도수가 높은 알파벳이 몇개인지

        # Traverse through tasks to calculate task frequencies
        for task in tasks:
            counter[ord(task) - ord('A')] += 1
            if max_val == counter[ord(task) - ord('A')]:
                max_count += 1
            elif max_val < counter[ord(task) - ord('A')]:
                max_val = counter[ord(task) - ord('A')]
                max_count = 1
        
        part_count = max_val - 1 # 가장 빈도가 높은 작업을 기준으로, 작업 사이의 슬롯을 계산하기 위해 max_val - 1을 저장합니다. 이는 가장 빈도가 높은 작업을 제외한 나머지 슬롯을 계산하기 위해 사용됩니다.
        part_length = n - (max_count - 1) # 각 슬롯의 길이를 계산하는데 사용되며, n - (max_count - 1)으로 계산합니다. 여기서 max_count - 1은 가장 빈도가 높은 작업들 사이에 들어갈 수 있는 슬롯을 의미합니다.
        empty_slots = part_count * part_length # 빈 슬롯의 총 개수는 part_count * part_length로 계산됩니다.
        available_tasks = len(tasks) - max_val * max_count # 빈 슬롯에 배치할 수 있는 나머지 작업 수 (전체 작업 수에서 가장 빈도가 높은 작업들을 제외한 수)
        idles = max(0, empty_slots - available_tasks) # 필요한 빈 슬롯에서 배치할 수 있는 작업을 제외한 나머지 빈 슬롯의 수를 계산합니다. 이 값이 0보다 작을 수 없으므로, 최소 0으로 설정됩니다.

        
        # 총 작업 수(len(tasks))와 필요한 대기시간(idles)을 더한 값입니다. 만약 대기 시간이 없으면, 그냥 총 작업 수가 최소 시간이 됩니다.
        return len(tasks) + idles
```