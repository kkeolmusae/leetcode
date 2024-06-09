class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      max_length = 0
      prev_idx = -1
      key_map = {}

      for idx in range(len(s)):
        st = s[idx]# 현재 문자
        
        if st in key_map and key_map[st] > prev_idx: # 과거에 처리한 문자면, 마지막으로 이 문자를 발견한 위치를 기점으로 현재까지 위치 계산
          prev_idx = key_map[st]
        key_map[st] = idx
        
        max_length = max(idx - prev_idx, max_length)

      return max_length