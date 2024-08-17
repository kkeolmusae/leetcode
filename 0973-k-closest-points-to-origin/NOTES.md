# 다른 풀이
(0,0)에서 거리가 가까운거 k개 리턴하는 문제
## 내 풀이 
- 시간복잡도: O(nlogn)
```py
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = [] # min heap
        for x, y in points:
            distance = (x**2 + y**2) ** 0.5 # 거리 계산해서
            heapq.heappush(q, (distance, [x, y])) # q에 넣기: O(n log n)

        result = []
        for _ in range(k): # O(k log n) (힙에서 k개의 요소를 꺼냄) 
            _, [x, y] = heapq.heappop(q) 
            result.append([x, y])

        return result
```

## 다른 풀이

### Sort (custom comparator)
시간 복잡도: O(nlogn)
```py
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort the list with a custom comparator function
        points.sort(key=self.squared_distance)
        
        # Return the first k elements of the sorted list
        return points[:k]
    
    def squared_distance(self, point: List[int]) -> int:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2
```

### Binary Search
- 이 코드는 이진 탐색과 유사한 방법을 사용하여 k개의 가장 가까운 점을 찾습니다.
- 효율적인 거리 비교를 위해 실제 거리를 계산하는 대신 제곱된 거리를 사용합니다.
- 이진 탐색을 통해 반복적으로 거리 범위를 줄여나가며, k개의 점을 점진적으로 찾아갑니다.
```py
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 각 점에 대한 유클리드 거리를 미리 계산
        distances = [self.euclidean_distance(point) for point in points]
        # 점의 인덱스로 이루어진 참조 리스트 생성
        remaining = [i for i in range(len(points))]
        # 이진 탐색의 초기 범위 설정
        low, high = 0, max(distances)
        
        # 이진 탐색을 수행하여 k개의 가장 가까운 점 찾기
        closest = []
        while k:
            mid = (low + high) / 2
            closer, farther = self.split_distances(remaining, distances, mid)
            if len(closer) > k:
                # 더 가까운 거리에 k개 이상의 점이 있는 경우
                # 더 먼 점들을 버리고 계속 탐색
                remaining = closer
                high = mid
            else:
                # 더 가까운 점들을 결과 배열에 추가하고
                # 남은 점들에 대해 더 먼 거리에서 계속 탐색
                k -= len(closer)
                closest.extend(closer)
                remaining = farther
                low = mid
                
        # 참조 인덱스를 사용해 k개의 가장 가까운 점 반환
        return [points[i] for i in closest]

    def split_distances(self, remaining: List[int], distances: List[float],
                        mid: int) -> List[List[int]]:
        """거리를 중간값 기준으로 나누고
        각각의 리스트로 반환."""
        closer, farther = [], []
        for index in remaining:
            if distances[index] <= mid:
                closer.append(index)
            else:
                farther.append(index)
        return [closer, farther]

    def euclidean_distance(self, point: List[int]) -> float:
        """제곱 유클리드 거리 계산 및 반환."""
        return point[0] ** 2 + point[1] ** 2
```