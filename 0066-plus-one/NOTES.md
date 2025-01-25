# 풀이
- Difficulty:  Easy
- Topic:  Math & Geometry
- Elapsed Time:  4m
- Status:  O 
- Memo:  그냥 쉬운 문제

## 내 풀이
```py
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(str(n) for n in digits))
        num2 = num + 1
        return [int(n) for n in str(num2)]
```

## 다른 풀이
### Approach 1: Schoolbook Addition with Carry
```py
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n):
            idx = n - 1 - i

            if digits[idx] == 9:
                digits[idx] = 0

            else:
                digits[idx] += 1

                return digits

        return [1] + digits
```
