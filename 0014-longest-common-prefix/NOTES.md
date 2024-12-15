# 풀이
- Difficulty:  Easy
- Topic:  Array / String
- Elapsed Time:  8m
- Status:  O (2 times)
- Memo: 어떻게 하면 더 효율적으로 풀까 고민하다가 시간이 좀 더 걸린듯 하다.

## 내 풀이
```py
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 1:  # 단어가 하나인 경우 
            return strs[0]

        same = 0  # 공통된 문자를 사용하는 개수

        # 우선 첫번째 단어랑 두번째 단어만 비교
        for idx in range(min(len(strs[0]), len(strs[1]))):
            if strs[0][same] == strs[1][same]:
                same += 1
            else:
                break

        # 그 다음부터는 두번째 단어랑 세번째 단어 비교 
        # (리팩토링: 두번째꺼랑 비교하는게 아니라 strs[0][:same] 이랑 새로운단어랑 비교하게 하는게 깔끔할듯)
        for idx in range(1, n - 1):
            if strs[idx][:same] != strs[idx + 1][:same]:
                cnt = 0
                for iidx in range(min(len(strs[idx]), len(strs[idx + 1]))):
                    if strs[idx][iidx] == strs[idx + 1][iidx]:
                        cnt += 1
                    else:
                        break
                same = cnt
        return strs[0][:same]
```

## 다른 풀이
### Approach 1: Horizontal scanning 
첫번째 문자열을 초기 접두사로 설정한 다음 두번쨰 문자열부터 비교
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 문자열 리스트가 비어있는 경우, 공통 접두사가 없으므로 빈 문자열 반환
        if len(strs) == 0:
            return ""

        # 첫 번째 문자열을 초기 접두사로 설정
        prefix = strs[0]
        
        # 두 번째 문자열부터 마지막 문자열까지 순회
        for i in range(1, len(strs)):
            # 현재 접두사가 strs[i]의 접두사가 아닐 때까지 반복
            while strs[i].find(prefix) != 0:
                # 접두사의 길이를 한 글자씩 줄임
                prefix = prefix[0 : len(prefix) - 1]
                # 접두사가 비어 있으면 빈 문자열 반환
                if prefix == "":
                    return ""
        
        # 최종적으로 남은 접두사를 반환
        return prefix

```

### Approach 2: Vertical scanning
한 문자씩 전체 문자열을 비교
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 문자열 리스트가 비어 있거나 None인 경우 공통 접두사가 없으므로 빈 문자열 반환
        if strs == None or len(strs) == 0:
            return ""

        # 첫 번째 문자열의 각 문자를 기준으로 탐색
        for i in range(len(strs[0])):
            # 첫 번째 문자열의 i번째 문자를 기준으로 설정
            c = strs[0][i]
            
            # 나머지 문자열들과 비교
            for j in range(1, len(strs)):
                # i가 현재 문자열의 길이를 초과하거나, i번째 문자가 첫 번째 문자열의 i번째 문자와 다르면
                if i == len(strs[j]) or strs[j][i] != c:
                    # 지금까지의 접두사를 반환
                    return strs[0][0:i]
        
        # 모든 문자열이 첫 번째 문자열과 같을 경우, 첫 번째 문자열 전체를 반환
        return strs[0]

```