# 풀이
​n 을 입력받으면 0 ~ n 까지의 숫자의 이진수의 "1" 의 개수를 찾는 문제.

## 내 풀이
간단하게 0 ~ n 까지의 숫자를 이진수로 바꾸고 "1"을 count 했다. dp 로 풀릴 것도 같았다.

```py
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            result.append(bin(i).count("1"))
        return result
```

## 다른 풀이

### Approach 1: Pop Count
191-number-of-1-bits 문제의 hammingWeight 함수를 여러번 사용해서 해결하는 방법
```py
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def pop_count(x: int) -> int:
            count = 0
            while x != 0:
                x &= x - 1 # 비트 연산: x &= x - 1은 x의 가장 오른쪽에 있는 1 비트를 제거합니다. 이 과정은 숫자 x에서 1이 더 이상 남아있지 않을 때까지 반복됩니다.
                count += 1
            return count
            
        ans = [0] * (n + 1)
        for x in range(n + 1):
            ans[x] = pop_count(x)
    
        return ans                                
```

### Approach 2: DP + Most Significant Bit
```py
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        x = 0
        b = 1
        
        # 범위 [b, 2b) 또는 [b, n]을 생성하면서 계속 확장
        while b <= n:
            # 이전 범위 [0, b)의 값들을 복사하여 새로운 범위 [b, 2b) 또는 [b, n]을 계산합니다.
            # ans[x + b] = ans[x] + 1: 이전에 계산된 값 ans[x]에 1을 더하여 새로운 값 ans[x + b]를 설정합니다. 
            # 이는 숫자 x + b가 x의 값에 1 비트를 추가한 것이기 때문입니다.
            while x < b and x + b <= n:
                ans[x + b] = ans[x] + 1
                x += 1
            x = 0 # 복사할 범위 초기화
            b <<= 1 # b *= 2
            
        return ans               
```

### Approach 3: DP + Least Significant Bit
- x >> 1: 이는 x를 오른쪽으로 1비트 이동시키는 연산입니다. 이는 곧 x // 2와 동일합니다. 예를 들어, x = 6 (이진수로 110)이면, x >> 1은 11이 되어 3이 됩니다.
- x & 1: 이는 x의 마지막 비트가 1인지 0인지를 확인하는 연산입니다. 즉, x % 2와 동일합니다. 이 값이 1이면 1비트가 추가되고, 0이면 추가되지 않습니다.
#### 예시 1: x = 5
- x = 5일 때, 이진수는 101입니다.
- x >> 1 = 5 // 2 = 2, 이진수로 10이므로 ans[2] = 1입니다.
- x & 1 = 5 % 2 = 1이므로, 마지막 비트가 1입니다.
- 따라서 ans[5] = ans[2] + 1 = 1 + 1 = 2입니다.

#### 예시 2: x = 6
- x = 6일 때, 이진수는 110입니다.
- x >> 1 = 6 // 2 = 3, 이진수로 11이므로 ans[3] = 2입니다.
- x & 1 = 6 % 2 = 0이므로, 마지막 비트는 0입니다.
- 따라서 ans[6] = ans[3] + 0 = 2 + 0 = 2입니다.

```py
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x >> 1] + (x & 1) 
        return ans 
```


### Approach 4: DP + Last Set Bit
- x & (x - 1)은 숫자 x의 이진수에서 가장 오른쪽에 있는 1비트를 제거한 숫자를 구하는 연산입니다.
- 이 연산의 결과는 x에서 마지막 1비트를 없앤 값이므로, 그 값을 이미 알고 있는 ans 리스트에서 가져와서, 그 결과에 1을 더해주면 현재 숫자 x의 1비트 개수를 구할 수 있습니다.
- 예를 들어, x = 6일 때, 6의 이진수는 110입니다. 6 & (6 - 1) = 6 & 5 = 110 & 101 = 100, 즉 4가 됩니다. 따라서 ans[6] = ans[4] + 1로 계산됩니다.
```py
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        return ans 
```