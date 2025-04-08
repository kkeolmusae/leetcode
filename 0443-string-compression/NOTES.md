# 풀이
- Difficulty:  Medium
- Topic:  Array / String
- Elapsed Time:  10m
- Status:  O (2 times)
- Approach:  in-place (입력 크기에 비례하는 추가 공간을 필요로 하지 않고 입력 데이터 구조 에서 직접 작동) 로 품
- Memo:  이전에는 추가 공간 할당해서 압축결과 만든다음에 결과를 char 에 넣는 방법으로 대충 풀었는데 이번에는 정정당당하게 in-place 방법으로 해겨함

## 내 풀이
```py
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0  # 압축된 결과를 적을 인덱스
        cnt = 1

        # 첫 문자부터 끝까지 순회
        for cidx in range(1, len(chars)):
            if chars[cidx] == chars[cidx - 1]:
                cnt += 1  # 연속 문자일 경우 count 증가
            else:
                # 연속이 끝났을 때 처리
                chars[i] = chars[cidx - 1]  # 문자 쓰기
                i += 1
                if cnt > 1:
                    for c in str(cnt):  # count가 2 이상이면 숫자도 문자로 써줌
                        chars[i] = c
                        i += 1
                cnt = 1  # count 초기화

        # 마지막 문자 그룹 처리
        chars[i] = chars[-1]
        i += 1
        if cnt > 1:
            for c in str(cnt):
                chars[i] = c
                i += 1

        return i  # 압축 후의 길이 반환
```

## 다른 풀이
### Approach
뭔가 이런 식의 해답을 원하는 듯 함....
```py
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0  # 현재 처리 중인 문자 위치를 추적하는 인덱스
        res = 0  # 압축된 결과를 저장할 위치를 추적하는 인덱스
        
        while i < len(chars):
            group_length = 1  # 현재 문자 그룹의 길이 (중복된 문자 수)
            
            # 현재 문자와 같은 문자가 연속으로 몇 번 나타나는지 계산
            while (i + group_length < len(chars)
                   and chars[i + group_length] == chars[i]):
                group_length += 1
            
            # 현재 문자를 결과 배열에 저장
            chars[res] = chars[i]
            res += 1
            
            # 그룹 길이가 1보다 큰 경우, 길이를 문자열로 변환하여 결과에 추가
            if group_length > 1:
                str_repr = str(group_length)
                chars[res:res+len(str_repr)] = list(str_repr)  # 숫자를 문자 리스트로 변환해 삽입
                res += len(str_repr)
            
            # 다음 그룹으로 이동
            i += group_length
        
        # 결과 배열의 길이 반환
        return res
```