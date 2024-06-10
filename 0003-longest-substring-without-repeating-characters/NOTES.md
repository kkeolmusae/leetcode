### NOTES
이거 처음에 슬라이딩 윈도우 방식으로 전체 배열 -> 점점 작아지는 방법으로 풀었는데 `TIME LIMIT EXEEDED` 에러 발생함.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      if len(s) < 2:
        return len(s)
      
      s_len = len(s)
      max_len = 0
      
      window_size = s_len

      idx1 = 0
      idx2 = s_len # 처음엔 최대 길이로 보고

      while window_size >= 0:
        if idx2 > s_len: # 배열 넘어가면
          window_size -= 1
          idx1 = 0
          idx2 = window_size
          continue

        dic = {}
        flag = True
        curr_str = s[idx1: idx2] # 체크하고자 하는 문자열

        for str in curr_str:
          if str in dic:
            idx1 += 1
            idx2 += 1
            flag = False
            break
          else:
            dic[str] = 1

        if flag:
          max_len = max(max_len, len(curr_str))
          break
        
      
      return max_len
```

그래서 다른코드 보고 다시 풀었는데 기가 막힘. 