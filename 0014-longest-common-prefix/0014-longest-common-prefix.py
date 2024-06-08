class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      if len(strs) == 1:
        return strs[0]

      result = ""
      flag = True
      idx = 0

      while flag:
        if len(strs[0]) == 0 or idx >= len(strs[0]): # 첫번째 문자의 길이가 0 이거나, 첫번째 문자의 길이보다 idx가 커지면 끝
          break

        temp = strs[0][idx]

        for i in range(1, len(strs)): # 두번째 문자부터 쭉 처리
          str = strs[i]
          
          if len(str) <= idx or temp != str[idx]: # n번째 문자의 길이가 idx보다 작거나 비교하고자 하는 문자가 다르면 끝
            flag = False
            break
        
        if flag:
          result += temp
          idx += 1
        
      return result