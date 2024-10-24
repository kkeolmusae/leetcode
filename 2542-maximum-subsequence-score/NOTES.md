# 풀이
- LeetCode 75, Medium
- Heap / Priority Queue
- Time: X
- 어려웠음. 처음에 heapq 어떻게 써야할지 모르겠어서 combinations 썼다가 메모리 초과 발생하고, 고민하다가 결국 해설지봄.

## 내 풀이 (해설지 보고 이해한 다음에 다시 품)
```py
class Solution:

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # nums1[i] 랑 nums2[i] 의 pair로 묶음
        pairs = [(a, b) for a, b in zip(nums1, nums2)]

        # nums2의 값으로 내림차순 정렬.
        # 왜냐하면 nums2에서 k개의 값중 최소값을 곱해야하는데 "num2의 k개 묶음"의 최솟값이 최대값이되는걸 찾기 위함
        pairs.sort(key=lambda x: -x[1])

        k_num1 = [x[0] for x in pairs[:k]]  # nums1 k개 꺼내고
        k_num1_sum = sum(k_num1)  # 합 계산
        heapq.heapify(k_num1)  # heapq로 변환(n1 작은거 부터 빼기위함)

        # 일단 pairs[0] ~ pairs[k-1] 에 대한 결과를 초기값으로 해두고 뒤에 k+1 ~ 갱신
        result = k_num1_sum * pairs[k - 1][1]

        # k 부터
        for n1, n2 in pairs[k : len(nums1)]:
            k_num1_sum -= heapq.heappop(k_num1)  # n1중에 작은거 빼고
            k_num1_sum += n1  # 새로 들어온거 추가하고
            heapq.heappush(k_num1, n1)  # k_num1 갱신

            # 최대값 갱신. pairs는 num2 기준 내림차순이라 n2가 최소값
            result = max(result, k_num1_sum * n2)

        return result

```

## 다른 풀이
### Approach: Priority Queue
이 코드는 nums2의 값이 큰 쌍을 우선 선택하고, 선택된 k개의 nums1 값들의 합을 사용하여 가능한 최대 점수를 계산합니다. nums2 값을 기준으로 정렬한 후, 최소 힙을 사용하여 효율적으로 k개의 요소를 관리함으로써 점수를 최대화합니다.
```py
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # 먼저 nums1과 nums2의 요소들을 zip을 사용하여 (nums1[i], nums2[i]) 형식의 쌍으로 만듭니다.
        # 그런 다음, 이 쌍들을 nums2[i] 값에 따라 내림차순으로 정렬합니다. 이는 nums2의 큰 값을 우선적으로 고려하기 위함입니다.
        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        pairs.sort(key = lambda x: -x[1])
        
        # 정렬된 쌍들 중에서 k개의 nums1 값을 추출하여 최소 힙(min-heap)으로 만듭니다. 이 힙은 현재 선택된 k개의 nums1 값들 중에서 가장 작은 값을 빠르게 찾기 위함입니다.
        top_k_heap = [x[0] for x in pairs[:k]]
        top_k_sum = sum(top_k_heap)
        heapq.heapify(top_k_heap)
        
        # 초기 점수는 첫 k개의 요소에서 nums1 값들의 합(top_k_sum)에 이들의 최소값 nums2[k-1][1]를 곱한 값입니다.
        answer = top_k_sum * pairs[k - 1][1]
        
        # 각 단계에서 가장 작은 nums1 값을 힙에서 제거하고 새로운 값을 추가합니다.
        for i in range(k, len(nums1)):
            # 업데이트된 top_k_sum과 현재 nums2[i] 값을 곱한 점수를 계산하고, 현재까지의 최대 점수와 비교하여 최대값을 유지합니다.
            top_k_sum -= heapq.heappop(top_k_heap)
            top_k_sum += pairs[i][0]
            heapq.heappush(top_k_heap, pairs[i][0])
            
            answer = max(answer, top_k_sum * pairs[i][1])
        
        return answer
            
```
