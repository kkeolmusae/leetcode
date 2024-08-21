# 풀이
- LeetCode 75, Medium
- Array / String
- Time: 22m
- 풀긴 했는데 좀 이상하게 품

## 내 풀이
문재 조건이 기존 배열(chars)를 활용해서 문자열을 압축하는건데 나는 걍 따로 압축 다 하고 마지막에 업데이트 하는 방법으로 품.
```py
class Solution:
    def compress(self, chars: List[str]) -> int:
        prev_ch = ""
        cnt = 0

        result = ""
        for c in chars:
            if c != prev_ch:  # 이전 문자랑 다르면
                result += prev_ch  # 이전문자 더해주고
                if cnt > 1:  # 중복된 숫자가 있으면 그 숫자만큼 더해주고
                    result += str(cnt)
                prev_ch = c  # 문자 및 중복 카운트 초기화
                cnt = 1
            else:
                cnt += 1  # 중복된 문자면 중복 카운트 증가

        result += prev_ch  # 나머지 처리
        if cnt > 1:
            result += str(cnt)

        for idx in range(len(result)):  # 문제 요구사항대로 기존 배열 업데이트
            chars[idx] = result[idx]

        return len(result)  # 압축한 문자 길이 반환
```

## 다른 풀이
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