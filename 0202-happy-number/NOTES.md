# 풀이
- Difficulty:  Easy
- Topic:  Hashmap
- Elapsed Time:  5m
- Status:  O
- Memo: 문제를 제대로 이해하지 못해서 시간이 조금 더 걸렸다.

## 내 풀이
hashmap을 사용하여 같은 숫자가 반복되면 Happy Number 가 아니다.
```py
class Solution:
    def isHappy(self, n: int) -> bool:
        hashmap = set()  # 같은 숫자 2번 반복하면 UnHappy임

        while True:
            tmp = list(str(n))
            next_n = 0
            for t in tmp:
                next_n += int(t) ** 2

            if next_n in hashmap:
                break
            hashmap.add(next_n)
            n = next_n
        return True if n == 1 else False
```

## 다른 풀이
### Approach 1: Detect Cycles with a HashSet
```py
class Solution:
    def isHappy(self, n: int) -> bool:

        # 다음 숫자를 계산하는 함수 정의
        def get_next(n):
            total_sum = 0  # 각 자리수의 제곱의 합을 저장할 변수
            while n > 0:
                # divmod(12345,10) => (1234, 5)
                n, digit = divmod(n, 10)  # n을 10으로 나눈 몫과 나머지를 구함  

                total_sum += digit**2  # 각 자리수의 제곱을 더함
            return total_sum  # 계산된 합 반환

        seen = set()  # 이미 확인한 숫자를 저장할 집합
        while n != 1 and n not in seen:  # n이 1이 아니고, 이미 확인한 숫자가 아닐 때 반복
            seen.add(n)  # 현재 숫자를 집합에 추가
            n = get_next(n)  # 다음 숫자를 계산
        
        return n == 1  # 숫자가 1이면 True, 아니면 False 반환

```

### Approach 2: Floyd's Cycle-Finding Algorithm
플로이드 알고리즘 사용. "사이클"이 생기는지 탐지하기 위해 두 포인터(slow_runner와 fast_runner)를 사용함
```py
class Solution:
    def isHappy(self, n: int) -> bool:
        # 다음 숫자를 계산하는 함수 정의
        def get_next(number):
            total_sum = 0  # 각 자리수의 제곱의 합을 저장할 변수
            while number > 0:
                number, digit = divmod(number, 10)  # number를 10으로 나눈 몫과 나머지를 구함
                total_sum += digit**2  # 각 자리수의 제곱을 더함
            return total_sum  # 계산된 합 반환

        slow_runner = n  # 느리게 움직이는 포인터
        fast_runner = get_next(n)  # 빠르게 움직이는 포인터

        # 두 포인터가 1에 도달하거나 서로 만나지 않을 때까지 반복
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)  # 느린 포인터는 한 번 이동
            fast_runner = get_next(get_next(fast_runner))  # 빠른 포인터는 두 번 이동

        return fast_runner == 1  # 빠른 포인터가 1에 도달하면 True 반환

```

### Approach 3: Hardcoding the Only Cycle (Advanced)
행복하지 않은 숫자를 하드코딩하여 답을 구함
```py
class Solution:
    def isHappy(self, n: int) -> bool:

        # 행복하지 않은 숫자에서 발생하는 사이클의 구성원들을 집합으로 정의
        cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}

        # 다음 숫자를 계산하는 함수 정의
        def get_next(number):
            total_sum = 0  # 각 자리수의 제곱의 합을 저장할 변수
            while number > 0:
                number, digit = divmod(number, 10)  # number를 10으로 나눈 몫과 나머지를 구함
                total_sum += digit**2  # 각 자리수의 제곱을 더함
            return total_sum  # 계산된 합 반환

        # n이 1이 아니고, 사이클 구성원에 포함되지 않을 때까지 반복
        while n != 1 and n not in cycle_members:
            n = get_next(n)  # 다음 숫자를 계산
        
        # n이 1이면 True, 아니면 False 반환
        return n == 1

```