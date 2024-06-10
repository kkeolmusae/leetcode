class Solution:
    def checkPalindrome(s, i, j):
      while i < j:
        if s[i] != s[j]:
          return False
        i += 1
        j -= 1
      
      return True

    def validPalindrome(self, s: str) -> bool:
      if len(s) == 1: 
        return True
      
      l_idx = 0
      r_idx = len(s) -1
      
      while l_idx < r_idx:
        if s[l_idx] != s[r_idx]:
          return Solution.checkPalindrome(s, l_idx + 1, r_idx) or Solution.checkPalindrome (s, l_idx, r_idx - 1)
        l_idx += 1
        r_idx -= 1

      return True