# 풀이
- Difficulty:  Medium
- Topic:  Heap
- Elapsed Time: X
- Status:  X
- Memo: 고민하다가 결국 시간초과로 못풀고 다른 사람의 힌트를 보고 풀었다. 다시 풀어보자.

## 내 풀이
처음에 nums1랑 nums2를 minheap 으로 만들고 하나씩 꺼내서 뭔가 조합하는 방법을 생각했는데 잘못된 접근 방법이었다. 다음은 힌트를 보고 해결한 코드
```py
class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:

        m = len(nums1)
        n = len(nums2)
        result = []

        visited = set()

        min_heap = [(nums1[0] + nums2[0], (0, 0))]  # 제일 앞에 있는 값 두개가 최소 값임
        visited.add((0, 0))  # 사용한 인덱스 저장

        while k > 0:
            _, (i, j) = heapq.heappop(min_heap)
            result.append(
                (nums1[i], nums2[j])
            )  # i,j 인덱스에 해당하는 값들을 result 에 추가

            #  i,j 가 가장 작은 조합이라면, 그 다음으로 작은 조합은 (i+1, j) 또는 (i, j+1) 이다.
            if i + 1 < m and (i + 1, j) not in visited:
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))
            k -= 1

        return result

```

## 다른 풀이
### Approach: Using Heap
```py
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        from heapq import heappush, heappop
        m = len(nums1)
        n = len(nums2)

        ans = []
        visited = set()

        minHeap = [(nums1[0] + nums2[0], (0, 0))]
        visited.add((0, 0))
        count = 0

        while k > 0 and minHeap:
            val, (i, j) = heappop(minHeap)
            ans.append([nums1[i], nums2[j]])

            if i + 1 < m and (i + 1, j) not in visited:
                heappush(minHeap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited:
                heappush(minHeap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))
            k = k - 1
        
        return ans
```