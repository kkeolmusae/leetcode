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
