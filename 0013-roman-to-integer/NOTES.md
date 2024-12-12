​# 풀이
- Difficulty:  Easy
- Topic:  Array / String
- Elapsed Time:  2m
- Status:  O (2 times)
- Memo: 몰랐는데 6개월전에 풀었던 문제임. 

## 내 풀이
이전에 while 문써서 좀 복잡하게 풀었는데 이번엔 쉽게 품
```py
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = dic[s[0]]
        for idx in range(1, len(s)):
            total += dic[s[idx]]  # 일단 더하고

            # 만약 전에 있던 기호가 현재 기호보다 작으면
            if dic[s[idx - 1]] < dic[s[idx]]:
                # 전에 더한거 다시 빼서 원복하고, 한번 더 빼줌
                total -= (dic[s[idx - 1]]) * 2
        return total
```

## 다른 풀이
### Approach 1: Left-to-Right Pass
```py
values = {
    "I": 1,    # 로마 숫자 'I'는 정수 1
    "V": 5,    # 로마 숫자 'V'는 정수 5
    "X": 10,   # 로마 숫자 'X'는 정수 10
    "L": 50,   # 로마 숫자 'L'은 정수 50
    "C": 100,  # 로마 숫자 'C'는 정수 100
    "D": 500,  # 로마 숫자 'D'는 정수 500
    "M": 1000  # 로마 숫자 'M'은 정수 1000
}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0  # 최종 정수를 저장할 변수
        i = 0      # 현재 문자열의 인덱스를 추적
        
        # 문자열 전체를 순회
        while i < len(s):
            # "감산 규칙"에 해당하는 경우 확인
            # 현재 문자(s[i])의 값이 다음 문자(s[i+1])의 값보다 작은 경우
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                # 다음 문자의 값에서 현재 문자의 값을 뺀 값을 더함
                total += values[s[i + 1]] - values[s[i]]
                i += 2  # 두 문자를 처리했으므로 인덱스를 2 증가
            else:
                # 감산 규칙이 아닌 경우, 현재 문자의 값을 더함
                total += values[s[i]]
                i += 1  # 한 문자만 처리했으므로 인덱스를 1 증가
        
        return total  # 최종 정수 값 반환

```

### Approach 2: Left-to-Right Pass Improved
```py
values = {
    "I": 1,    # 로마 숫자 'I'는 정수 1
    "V": 5,    # 로마 숫자 'V'는 정수 5
    "X": 10,   # 로마 숫자 'X'는 정수 10
    "L": 50,   # 로마 숫자 'L'은 정수 50
    "C": 100,  # 로마 숫자 'C'는 정수 100
    "D": 500,  # 로마 숫자 'D'는 정수 500
    "M": 1000, # 로마 숫자 'M'은 정수 1000
    "IV": 4,   # 감산 규칙: 'IV'는 4
    "IX": 9,   # 감산 규칙: 'IX'는 9
    "XL": 40,  # 감산 규칙: 'XL'은 40
    "XC": 90,  # 감산 규칙: 'XC'는 90
    "CD": 400, # 감산 규칙: 'CD'는 400
    "CM": 900  # 감산 규칙: 'CM'은 900
}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0  # 최종 정수를 저장할 변수
        i = 0      # 현재 문자열의 인덱스를 추적

        # 문자열 전체를 순회
        while i < len(s):
            # 감산 규칙에 해당하는 경우 (2글자 조합이 values에 있는지 확인)
            if i < len(s) - 1 and s[i : i + 2] in values:
                total += values[s[i : i + 2]]  # 두 글자 조합의 값을 더함
                i += 2  # 두 문자를 처리했으므로 인덱스를 2 증가
            else:
                # 감산 규칙이 아닌 경우, 한 글자의 값을 더함
                total += values[s[i]]
                i += 1  # 한 문자만 처리했으므로 인덱스를 1 증가
        
        return total  # 최종 정수 값 반환

```

### Approach 3: Right-to-Left Pass
```py
values = {
    "I": 1,    # 로마 숫자 'I'는 정수 1
    "V": 5,    # 로마 숫자 'V'는 정수 5
    "X": 10,   # 로마 숫자 'X'는 정수 10
    "L": 50,   # 로마 숫자 'L'은 정수 50
    "C": 100,  # 로마 숫자 'C'는 정수 100
    "D": 500,  # 로마 숫자 'D'는 정수 500
    "M": 1000  # 로마 숫자 'M'은 정수 1000
}


class Solution:
    def romanToInt(self, s: str) -> int:
        # 문자열의 마지막 문자의 값을 초기 총합으로 설정
        total = values.get(s[-1])

        # 문자열을 뒤에서 두 번째 문자부터 순회
        for i in reversed(range(len(s) - 1)):
            # 현재 문자가 다음 문자보다 작으면 (감산 규칙)
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]  # 현재 문자의 값을 뺌
            else:
                total += values[s[i]]  # 그렇지 않으면 현재 문자의 값을 더함
        
        return total  # 최종 결과 반환

```