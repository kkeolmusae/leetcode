# 풀이
- Difficulty:  Medium
- Topic:  Heap / Priority Queue
- Elapsed Time:  4m
- Status:  O (2 times)
- Memo: 쉬웠음

## 내 풀이
```py
class Solution:
    def euclideanDist(self, x, y):
        return math.sqrt((0 - y) ** 2 + (0 - x) ** 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        result = []

        for x, y in points:
            r = self.euclideanDist(x, y)
            heapq.heappush(q, (r, (x, y)))

        while k:
            _, (x, y) = heapq.heappop(q)
            result.append([x, y])
            k -= 1
        return result
```

## 다른 풀이
### Approach 1: Sort with Custom Comparator
- 시간 복잡도: O(nlogn)
```py
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 점들을 제곱 거리 기준으로 정렬
        points.sort(key=self.squared_distance)
        
        # 가장 가까운 k개의 점 반환
        return points[:k]
    
    def squared_distance(self, point: List[int]) -> int:
        # 점의 제곱 거리 계산 (원점으로부터)
        return point[0] ** 2 + point[1] ** 2

```

### Approach 2: Max Heap or Max Priority Queue
```py
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 처음 k개의 점을 기반으로 최대 힙 생성 (음수 값으로 저장하여 최대 힙처럼 동작)
        heap = [(-self.squared_distance(points[i]), i) for i in range(k)]
        heapq.heapify(heap)
        
        # 나머지 점들을 순회하며 힙에 삽입/제거
        for i in range(k, len(points)):
            dist = -self.squared_distance(points[i])  # 제곱 거리를 음수로 변환
            if dist > heap[0][0]:  # 힙의 루트(최대값)보다 거리가 작으면 업데이트
                heapq.heappushpop(heap, (dist, i))
        
        # 힙에 남아있는 k개의 점 반환
        return [points[i] for (_, i) in heap]
    
    def squared_distance(self, point: List[int]) -> int:
        # 점의 제곱 거리 계산 (원점으로부터)
        return point[0] ** 2 + point[1] ** 2
```

### Approach 3: Binary Search
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

### Approach 4: QuickSelect
```py
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # QuickSelect 알고리즘을 사용하여 k개의 가장 가까운 점을 찾음
        return self.quick_select(points, k)
    
    def quick_select(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        QuickSelect 알고리즘을 수행하여 가장 가까운 k개의 점을 찾음
        """
        left, right = 0, len(points) - 1
        pivot_index = len(points)  # 초기 pivot_index를 점 개수로 설정
        while pivot_index != k:
            # 리스트를 pivot 기준으로 분할
            pivot_index = self.partition(points, left, right)
            if pivot_index < k:
                # k가 더 오른쪽에 있다면 left 포인터를 이동
                left = pivot_index
            else:
                # k가 더 왼쪽에 있다면 right 포인터를 이동
                right = pivot_index - 1
        
        # 가장 가까운 k개의 점 반환
        return points[:k]
    
    def partition(self, points: List[List[int]], left: int, right: int) -> int:
        """
        pivot을 기준으로 리스트를 분할
        pivot보다 작은 값은 왼쪽에, 큰 값은 오른쪽에 배치
        """
        pivot = self.choose_pivot(points, left, right)  # pivot 점 선택
        pivot_dist = self.squared_distance(pivot)  # pivot의 제곱 거리 계산
        
        while left < right:
            if self.squared_distance(points[left]) >= pivot_dist:
                # 왼쪽 값이 pivot보다 크다면 오른쪽으로 이동
                points[left], points[right] = points[right], points[left]
                right -= 1
            else:
                # pivot보다 작거나 같다면 left 증가
                left += 1
        
        # pivot 위치를 조정
        if self.squared_distance(points[left]) < pivot_dist:
            left += 1
        return left
    
    def choose_pivot(self, points: List[List[int]], left: int, right: int) -> List[int]:
        """
        리스트에서 pivot 점을 선택
        중간 지점을 pivot으로 사용
        """
        return points[left + (right - left) // 2]
    
    def squared_distance(self, point: List[int]) -> int:
        """
        점의 제곱 유클리드 거리 계산
        """
        return point[0] ** 2 + point[1] ** 2
```