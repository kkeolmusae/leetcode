# 풀이
- Difficulty:  Medium
- Topic:  Array / String
- Elapsed Time:  7m
- Status:  O 
- Memo: 노트에 손코딩하고 나서 코드로 옮겼는데 생각보다 의도대로 풀렸다.

## 내 풀이
```py
class Solution:
    def intToRoman(self, num: int) -> str:
        ex_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ex_str = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        # 감산 규칙을 적용했을 때 만들 수 있는 숫자와 문자까지 포함해서 내림차순으로 미리 깔아놓고 시작했다.
        idx = 0

        result = ""
        while idx < len(ex_num) and num > 0:
            tmp = num // ex_num[idx]  # 현재 위치의 숫자로 나눠보고
            # 나눠져서 몫이 나오면
            if tmp > 0:
                result += tmp * ex_str[idx]  # tmp 만큼해당 숫자반복
                num -= ex_num[idx] * tmp
            else:
              # 나눴는데 몫이 0 이면 다음 숫자로 넘어감
                idx += 1

        return result
```

## 다른 풀이
### Approach 1: Greedy
내 코드처럼 감산 규칙을 적용한문자와 숫자까지 미리 튜플에 넣어놓고 계산했다. 
```py
class Solution:
    def intToRoman(self, num: int) -> str:
        # 로마 숫자와 대응하는 정수 값을 저장한 튜플 리스트
        digits = [
            (1000, "M"),   # 1000 -> M
            (900, "CM"),   # 900 -> CM
            (500, "D"),    # 500 -> D
            (400, "CD"),   # 400 -> CD
            (100, "C"),    # 100 -> C
            (90, "XC"),    # 90 -> XC
            (50, "L"),     # 50 -> L
            (40, "XL"),    # 40 -> XL
            (10, "X"),     # 10 -> X
            (9, "IX"),     # 9 -> IX
            (5, "V"),      # 5 -> V
            (4, "IV"),     # 4 -> IV
            (1, "I"),      # 1 -> I
        ]

        # 결과를 저장할 리스트
        roman_digits = []
        
        # 각 로마 숫자 심볼과 값을 순회
        for value, symbol in digits:
            # num 값이 0이면 루프 종료 (더 이상 변환할 필요 없음)
            if num == 0:
                break
            
            # 현재 값(value)로 나눈 몫과 나머지를 계산
            count, num = divmod(num, value)
            
            # 몫(count)만큼 해당 로마 숫자(symbol)을 결과 리스트에 추가
            roman_digits.append(symbol * count)
        
        # 리스트를 문자열로 결합하여 반환
        return "".join(roman_digits)

```

### Approach 2: Hardcode Digits
이건 그냥 하드코딩한 방식. 나도 내 의도대로 구현했는데 답이 틀렸으면 하드코딩하는 방법으로 구현했을 듯 하다.
```py
class Solution:
    def intToRoman(self, num: int) -> str:
        # 천의 자리 숫자에 해당하는 로마 숫자
        thousands = ["", "M", "MM", "MMM"]
        # 백의 자리 숫자에 해당하는 로마 숫자
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        # 십의 자리 숫자에 해당하는 로마 숫자
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        # 일의 자리 숫자에 해당하는 로마 숫자
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        
        # 각 자리 숫자에 해당하는 로마 숫자를 조합하여 반환
        return (
            thousands[num // 1000]          # 천의 자리
            + hundreds[num % 1000 // 100]  # 백의 자리
            + tens[num % 100 // 10]        # 십의 자리
            + ones[num % 10]               # 일의 자리
        )

```

### Approach 3:
```py
```

### Approach 4:
```py
```

### Approach 5:
```py
```