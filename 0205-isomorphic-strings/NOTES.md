# 풀이
- Difficulty:  Easy
- Topic:  Hashmap
- Elapsed Time:  4m
- Status:  O 
- Memo: 이것도 쉬웠음

## 내 풀이
```py
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s2t = {}  # s를 t로 바꾸는 매핑
        t2s = {}  # t를 s로 바꾸는 매핑

        for i in range(len(s)):
            # s를 t로 바꾸는 매핑이 이미 존재하고, t[i]와 다르다면 => False
            if s[i] in s2t and s2t[s[i]] != t[i]:
                return False
            # t를 s로 바꾸는 매핑이 이미 존재하고, t[i]와 다르다면 => False
            if t[i] in t2s and t2s[t[i]] != s[i]:
                return False

            s2t[s[i]] = t[i]  # s[i]를 t[i]로 바꾸는 매핑
            t2s[t[i]] = s[i]  # t[i]를 s[i]로 바꾸는 매핑
        return True
```

## 다른 풀이
### Approach 1: Character Mapping with Dictionary
zip 를 사용해서 풀었다. (zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환합니다.)

```py
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapping_s_t = {}
        mapping_t_s = {}

        for c1, c2 in zip(s, t):  # s랑 t 하나씩 꺼냄
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False

        return True
```

### Approach 2:
```py
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