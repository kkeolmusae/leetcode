​# 풀이
- Difficulty:  Easy
- Topic:  Hashmap
- Elapsed Time:  2m
- Status:  O (2 times)
- Memo: 0383 이랑 비슷한 문제

## 내 풀이
```py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_s = Counter(s)
        counter_t = Counter(t)

        for char, count in counter_s.items():
            if counter_t[char] != count:
                return False
        return True
```

## 다른 풀이
### Approach 1: Sorting
```java
public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) {
        return false;
    }
    char[] str1 = s.toCharArray();
    char[] str2 = t.toCharArray();
    Arrays.sort(str1);
    Arrays.sort(str2);
    return Arrays.equals(str1, str2);
}
```

### Approach 2: Frequency Counter
```java
public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) {
        return false;
    }
    int[] counter = new int[26];
    for (int i = 0; i < s.length(); i++) {
        counter[s.charAt(i) - 'a']++;
        counter[t.charAt(i) - 'a']--;
    }
    for (int count : counter) {
        if (count != 0) {
            return false;
        }
    }
    return true;
}
```