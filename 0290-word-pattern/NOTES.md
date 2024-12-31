# 풀이
- Difficulty:  Easy
- Topic:  Hashmap
- Elapsed Time:  4m
- Status:  O
- Memo: 0205 문제랑 비슷함

## 내 풀이
```py
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split_s = s.split()
        if len(pattern) != len(split_s):
            return False

        pattern_dict = {}
        word_dict = {}

        for p, w in zip(pattern, split_s):  # 하나씩 꺼내서
            if p not in pattern_dict:  # 없으면 추가
                pattern_dict[p] = w
            else:
                if pattern_dict[p] != w:  # 있으면 dict에 있는 값과 비교
                    return False

            if w not in word_dict:
                word_dict[w] = p
            else:
                if word_dict[w] != p:
                    return False

        return True
```

## 다른 풀이
### Approach 1: Two Hash Maps
```py
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_char = {}
        map_word = {}
        
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        
        for c, w in zip(pattern, words):
            if c not in map_char:
                if w in map_word:
                    return False
                else:
                    map_char[c] = w
                    map_word[w] = c
            else:
                if map_char[c] != w:
                    return False
        return True
```

### Approach 2: Single Index Hash Map
```py
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_index = {}  # 각 문자와 단어의 인덱스를 저장할 맵
        words = s.split()  # 문자열 s를 공백 기준으로 나눠 단어 리스트로 만듦
        
        # 패턴의 길이와 단어 리스트의 길이가 다르면 False 반환
        if len(pattern) != len(words):
            return False
        
        # 패턴과 단어 리스트를 순회
        for i in range(len(words)):
            c = pattern[i]  # 현재 패턴의 문자
            w = words[i]    # 현재 문자열의 단어

            char_key = 'char_{}'.format(c)  # 패턴 문자를 키로 변환
            char_word = 'word_{}'.format(w)  # 단어를 키로 변환
            
            # 패턴 문자가 맵에 없으면 현재 인덱스를 저장
            if char_key not in map_index:
                map_index[char_key] = i
            
            # 단어가 맵에 없으면 현재 인덱스를 저장
            if char_word not in map_index:
                map_index[char_word] = i 
            
            # 패턴 문자와 단어의 인덱스가 다르면 False 반환
            if map_index[char_key] != map_index[char_word]:
                return False
        
        # 패턴이 일치하면 True 반환
        return True

```