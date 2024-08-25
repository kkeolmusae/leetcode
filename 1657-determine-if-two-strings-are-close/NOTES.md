# 풀이
- LeetCode 75, Medium
- Hash Map / Set
- Time: 10m
- 약간 고민하긴 했는데 대충 감을 잡고 나서는 금방 품. 잘짠 코드는 아닌듯

## 내 풀이
- 길이가 다르면 아예 불가능한거니깐 리턴하고, 서로 존재하는 문자가 다르면 그것도 걍 리턴 False하고
- 두 배열의 숫자개수를 count한 값을 정렬한다음에 비교했을떄 같으면 True 아니면 False
```py
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for w in list(word1):
            d1[w] += 1

        for w in list(word2):
            if w not in d1:  # 문자가 존재하지 않으면 걍 return False
                return False
            d2[w] += 1

        if sorted(d1.values()) == sorted(d2.values()):  # 정렬한 두 배열이 같으면 
            return True
        return False
```

## 다른 풀이
### Approach 1: Using HashMap
오 내 코드랑 거의 소름끼치게 비슷함. 의외로 정석이었을지도?
```py
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 두 단어의 길이가 다르면 false를 반환
        if len(word1) != len(word2):
            return False
        
        # 각 단어의 문자와 빈도를 저장할 딕셔너리
        word1_map = {}
        word2_map = {}
        
        # word1의 문자 빈도수를 딕셔너리에 저장
        for c in word1:
            word1_map[c] = word1_map.get(c, 0) + 1
        
        # word2의 문자 빈도수를 딕셔너리에 저장
        for c in word2:
            word2_map[c] = word2_map.get(c, 0) + 1
        
        # 두 단어의 문자가 동일한지 확인 (문자 집합 비교)
        if set(word1_map.keys()) != set(word2_map.keys()):
            return False
        
        # 각 단어의 문자 빈도수를 리스트로 변환하고 정렬
        word1_frequency_list = sorted(word1_map.values())
        word2_frequency_list = sorted(word2_map.values())
        
        # 두 리스트가 동일한지 확인 (빈도 리스트 비교)
        return word1_frequency_list == word2_frequency_list

```

### Approach 2: Using Frequency Array Map
Approach1 이랑 유사함. 2는 set대신 []사용함
```py
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 두 문자열의 길이가 다르면 false를 반환
        if len(word1) != len(word2):
            return False
        
        # 각 문자열의 문자 빈도를 저장할 리스트
        word1_map = [0] * 26
        word2_map = [0] * 26
        
        # word1의 문자 빈도수를 리스트에 저장
        for c in word1:
            word1_map[ord(c) - ord('a')] += 1
        
        # word2의 문자 빈도수를 리스트에 저장
        for c in word2:
            word2_map[ord(c) - ord('a')] += 1
        
        # 두 문자열에 존재하지 않는 문자가 있는지 확인
        for i in range(26):
            if (word1_map[i] == 0 and word2_map[i] > 0) or (word2_map[i] == 0 and word1_map[i] > 0):
                return False
        
        # 빈도수를 정렬하고 비교
        return sorted(word1_map) == sorted(word2_map)

```

### Approach 3: Using Bitwise Operation and Frequency Array Map
```py
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 두 문자열의 길이가 다르면 false를 반환
        if len(word1) != len(word2):
            return False
        
        # 각 문자열의 문자 빈도수를 저장할 리스트
        word1_map = [0] * 26
        word2_map = [0] * 26
        
        # 각 문자열에서 사용된 문자의 비트마스크를 저장할 변수
        word1_bit = 0
        word2_bit = 0
        
        # word1의 문자 빈도수와 비트마스크를 계산
        for c in word1:
            word1_map[ord(c) - ord('a')] += 1
            word1_bit |= 1 << (ord(c) - ord('a'))
        
        # word2의 문자 빈도수와 비트마스크를 계산
        for c in word2:
            word2_map[ord(c) - ord('a')] += 1
            word2_bit |= 1 << (ord(c) - ord('a'))
        
        # 두 문자열에서 사용된 문자의 종류가 같지 않으면 false를 반환
        if word1_bit != word2_bit:
            return False
        
        # 빈도수를 정렬하고 비교
        word1_map.sort()
        word2_map.sort()
        
        # 빈도수가 동일한지 확인
        return word1_map == word2_map

```