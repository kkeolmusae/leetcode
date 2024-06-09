class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        curr_node = result
        temp = 0 # 다음위치에 더해줄 수
        
        while l1 != None or l2 != None or temp != 0:
          l1_val = l1.val if l1 else 0 # l1 이 있으면 값, 아니면 0
          l2_val = l2.val if l2 else 0
          
          sum_val = l1_val + l2_val + temp
          temp = sum_val // 10 # 다음에 더해줄 거
          
          new_node = ListNode(sum_val % 10)
          curr_node.next = new_node # 뒤에 붙여주고
          curr_node = new_node # 현재 노드 바꿔주고
          
          l1 = l1.next if l1 else None # l1 노드 전진
          l2 = l2.next if l2 else None # l1 노드 전진
          
        return result.next