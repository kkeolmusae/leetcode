class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        curr = answer
        tmp = 0
        head = head.next

        while head:
            if head.val == 0:
                curr.next = ListNode(tmp)
                curr = curr.next
                tmp = 0
            else:
                tmp += head.val
            head = head.next

        return answer.next  