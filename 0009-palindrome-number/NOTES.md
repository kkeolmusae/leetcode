​# 풀이
- Difficulty:  Easy
- Topic:  Math
- Elapsed Time:  1m
- Status:  O (2 times)
- Approach:  
- Memo:  그냥 눈에 보이길래 쉽게 해결했다. Two Pointer 로 해결하는 방법도 있긴한데 그냥 쉽게 해결했다.

## 내 풀이
- [시작:끝:단계] 형식에서 시작과 끝을 비워두면 전체 문자열을 대상으로 합니다.
- 단계가 -1이므로, 문자열을 뒤에서부터 앞으로 한 글자씩 가져옵니다.
```py
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1] # 
```

## 다른 풀이
### Approach 1: Revert half of the number
```py
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 음수이거나, 0이 아닌 숫자가 0으로 끝나는 경우(예: 10, 20)는 회문이 될 수 없음
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0  # 뒤집은 숫자를 저장할 변수
        while x > revertedNumber:
            # x의 마지막 자릿수를 revertedNumber에 추가
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10  # x를 마지막 자릿수를 제외한 값으로 업데이트

        # 숫자가 짝수 자리일 때 (예: 1221) x == revertedNumber
        # 숫자가 홀수 자리일 때 (예: 121) x == revertedNumber // 10
        return x == revertedNumber or x == revertedNumber // 10

```