# 풀이
- Hard
- Heap (Priority Queue)
- Time: 10m
- ListNode 를 사용하는 방법을 몰라서 헤맨거 뺴고는 쉬웠음. 그냥 heapq 쓸줄 아는지 물어보는 수준

## 내 풀이
```py
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        head = point = ListNode(0)
        
        for l in lists:
            while l:
                heapq.heappush(q, l.val)
                l = l.next

        while q:
            point.next = ListNode(heapq.heappop(q))
            point = point.next
        return head.next

```

## 다른 풀이
### Approach 1: Brute Force
heapq 안쓰고 sorted 한다음 푸는 방법
```py
class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next

        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next

        return head.next
```

### Approach 2: Optimize Approach 2 by Priority Queue
내 코드랑 비슷함.
```py
class HeapNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        # Define comparison based on ListNode's value
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        heap = []

        # Initialize the heap
        for l in lists:
            if l:
                heapq.heappush(heap, HeapNode(l))

        # Extract the minimum node and add its next node to the heap
        while heap:
            heap_node = heapq.heappop(heap)
            node = heap_node.node
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, HeapNode(node.next))

        return dummy.next
```