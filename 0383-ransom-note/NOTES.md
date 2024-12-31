# 풀이
- Difficulty:  Easy
- Topic:  Hashmap
- Elapsed Time:  2m
- Status:  O
- Memo: 쉬운 문제

## 내 풀이
처음에 ransomNote.count(i) 처럼 썼다가 비효율적인것 같아서 Count(ransomNote)로 바꿈
```py
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        for char, count in ransom_counter.items():
            if magazine_counter[char] < count:
                return False
        return True


```

## 다른 풀이
### Approach 1: Two HashMaps
```py
def canConstruct(self, ransomNote: str, magazine: str) -> bool:

    if len(ransomNote) > len(magazine): return False

    magazine_counts = collections.Counter(magazine)
    ransom_note_counts = collections.Counter(ransomNote)
    
    for char, count in ransom_note_counts.items():
        magazine_count = magazine_counts[char]
        if magazine_count < count:
            return False
            
    return True
```
