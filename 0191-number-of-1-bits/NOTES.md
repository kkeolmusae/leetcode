# 풀이
이진수로 바꿨을때 1의 개수

## 내 풀이
n을 bin 함수를 이용하여 이진수로 바꾼 다음에 이진수의 1을 count 하는 방법으로 품
```py
from typing import List


class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n) # n = 11 => 0b1011
        return b.count("1")
```

## 다른 풀이
n 과 n-1을 and 연산(&) 으로 계산하여 오른쪽 1비트를 제거하는 방식으로 품
1. 11 (1011), 10 (1010) 을 & 하면 1010이 되고
2. 1010 과 1001 을 하면 1000 이 되고
3. 1000 100 을 하면 0000이 되어 
답은 3이 되는 원리
```py
class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        while n != 0:
            sum += 1
            n &= (n - 1)  # 가장 오른쪽에 있는 1 비트를 제거
        return sum

```