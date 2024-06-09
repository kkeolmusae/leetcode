### NOTES
이거 처음에 문제 잘못 읽어서 그냥 배열로 풀었다가 LinkedList 사용하는 방법으로 바꿔서 품
```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_size = len(l1)
        l2_size = len(l2)

        l1_l2_size = max(l1_size, l2_size) # 최대 배열 길이
        diff = abs(l1_size - l2_size) # 두 배열 길이의 차이

        if diff != 0: # 차이 나는 만큼 뒤에 붙여주고
          if l1_size > l2_size:
            l2 = l2 + [0] * diff
          else: 
            l1 = l1 + [0] * diff
        
        idx = 0
        result = [0] * (l1_l2_size + 1) 
        while idx < l1_l2_size:
          a = l1[idx] + l2[idx]

          result[idx] += a # 일단 더하고
          
          if result[idx] >= 10: # 10보다 많이 들어갔으면 
            result[idx + 1] = result[idx] // 10 # 몫 뒤에 붙여주고
            result[idx] = result[idx] % 10 # 나머지 처리
            
          idx += 1
        
        while result[len(result) - 1] == 0 and len(result) > 1:
          result.pop()
            
        return result
```

근데 파이썬에서 LinkedList 사용하는거 익숙하지 않아서 Solution 살짝 봄