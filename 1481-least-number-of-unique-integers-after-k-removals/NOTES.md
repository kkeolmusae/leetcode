# 다른 풀이 
### 내 풀이
시간 복잡도: O(n+mlogm)
```py
from typing import Counter, List
import heapq


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        q = []
        c = Counter(arr)

        for num in c:
            heapq.heappush(q, (c[num], num))  # 개수랑 숫자

        while k > 0:
            cnt, num = heapq.heappop(q)

            if cnt > k:
                return len(q) + 1
            elif cnt == k:
                return len(q)
            else:
                k -= cnt

        return len(q)
```

### 다른 풀이 1
시간복잡도: O(nlogn)
```py
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Dictionary to track the frequencies of elements
        freq_map = Counter(arr)

        # List to track all the frequencies
        frequencies = list(freq_map.values())

        # Sorting the frequencies
        frequencies.sort()

        # Tracking the number of elements removed
        elements_removed = 0

        for i in range(len(frequencies)):
            # Removing frequencies[i] elements, which equates to
            # removing one unique element
            elements_removed += frequencies[i]

            # If the number of elements removed exceeds k, return
            # the remaining number of unique elements
            if elements_removed > k:
                return len(frequencies) - i

        # We have removed all elements, so no unique integers remain
        # Return 0 in this case
        return 0
```

### 다른 풀이 2
시간 복잡도: O(nlogn)
```py
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Dictionary to track the frequencies of elements
        freq_map = Counter(arr)

        # Min heap to track all the frequencies
        frequencies = list(freq_map.values())
        heapq.heapify(frequencies)

        # Tracking the number of elements removed
        elements_removed = 0

        # Traversing all frequencies
        while frequencies:
            # Removing the least frequent element
            elements_removed += heapq.heappop(frequencies)

            # If the number of elements removed exceeds k, return
            # the remaining number of unique elements
            if elements_removed > k:
                # Add 1 for the remaining element
                return len(frequencies) + 1

        # We have removed all elements, so no unique integers remain
        # Return 0 in this case
        return 0
```

### 다른 풀이법 3
이건 이해 못해서 이해해야함... 
시간 복잡도: O(n)
```py
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # 1. 요소의 빈도수 계산
        map = {}
        for i in arr:
            map[i] = map.get(i, 0) + 1

        n = len(arr)

        # 2. 빈도수의 빈도수 계산
        # 빈도수의 빈도수를 추적하기 위한 리스트
        # 요소의 최대 빈도수는 n이므로 리스트의 크기를 n + 1로 초기화
        count_of_frequencies = [0] * (n + 1)

        # count_of_frequencies 리스트 채우기
        for count in map.values():
            count_of_frequencies[count] += 1

        # 3. 남아 있는 고유한 요소의 개수 초기화
        remaining_unique_elements = len(map)

        # 4. 빈도수별로 요소 제거
        # 가능한 모든 빈도수 i에 대해 반복합니다. 빈도수 i는 1부터 n까지입니다.
        # 각 빈도수 i에 대해 제거할 수 있는 최대 요소의 개수를 num_elements_to_remove로 계산합니다.
        # - k // i는 현재 남은 제거 가능 횟수 k로 빈도수 i인 요소를 몇 개 제거할 수 있는지를 나타냅니다.
        # - count_of_frequencies[i]는 빈도수 i인 요소의 실제 개수입니다.
        # - min(k // i, count_of_frequencies[i])는 실제로 제거할 수 있는 요소의 개수를 결정합니다.
        # 요소를 제거한 후 남은 k 값을 업데이트하고, 제거한 요소의 개수만큼 남은 고유한 요소의 개수를 감소시킵니다.
        # 만약 k가 현재 빈도수 i보다 작으면 더 이상 제거할 수 없으므로 남은 고유한 요소의 개수를 반환합니다.
        for i in range(1, n + 1):
            num_elements_to_remove = min(k // i, count_of_frequencies[i])
            k -= (i * num_elements_to_remove)
            remaining_unique_elements -= num_elements_to_remove

            if k < i:
                return remaining_unique_elements

        return 0
```