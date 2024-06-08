class Solution:
    def romanToInt(self, s: str) -> int:
      symbol_dic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
      }
  
      idx = len(s) - 1
      prev_symbol = s[idx]
      result = symbol_dic[prev_symbol] # 마지막 숫자 일단 더해놓기
      
      idx -= 1
      while idx >= 0:
        current_symbol = s[idx]
        
        if symbol_dic[current_symbol] < symbol_dic[prev_symbol]: # 현재 심볼이 이전 심볼보다 낮은거면 값에서 빼줘야함
          result -= symbol_dic[current_symbol]
        else:
          result += symbol_dic[current_symbol]
        prev_symbol = current_symbol

        idx -= 1

      return result