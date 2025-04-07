# 풀이
- Difficulty:  Easy
- Topic:  Array / String
- Elapsed Time:  3m 25s
- Status:  O (2 times)
- Approach:  -
- Memo:  쉬운문제. 다시 알고리즘 문제에 흥미를 붙이기위해 품

## 내 풀이
- 각 단어의 인덱스를 개별 포인터(w1_idx, w2_idx)로 관리하면서 교차로 문자를 합쳐나감.  
- 길이가 다른 경우를 고려해, 한 쪽이 먼저 끝나면 남은 문자열을 한 번에 붙여서 마무리.  
- 파이썬의 슬라이싱(`word[x:]`)을 적절히 활용하여 깔끔하게 처리함.
```py
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_idx = 0
        w2_idx = 0
        w1_len = len(word1)
        w2_len = len(word2)

        result = ""
        while w1_idx < w1_len and w2_idx < w2_len:
            result += word1[w1_idx]
            result += word2[w2_idx]
            w1_idx += 1
            w2_idx += 1

        if w1_idx < w1_len:
            result += word1[w1_idx:]
        elif w2_idx < w2_len:
            result += word2[w2_idx:]

        return result
```

## 다른 풀이
### Approach 1:
```py
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