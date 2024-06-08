class Solution:
    def isPalindrome(self, x: int) -> bool:
      if x < 0: # 음수면 Palindrome 아님
        return False

      str_num = str(x)
      str_num_len = len(str_num)
      
      l_idx = 0
      r_idx = str_num_len - 1
      
      while l_idx != r_idx and l_idx < r_idx:
        l_num = str_num[l_idx]
        r_num = str_num[r_idx]
        
        if l_num != r_num:
          return False
        
        l_idx += 1
        r_idx -= 1
      
      return True