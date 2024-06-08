class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      dic = {}
      nums.sort()
      
      for num in nums:
        if num not in dic: 
          dic[num] = 1
        else:
          dic[num] += 1
      
      s = set()
      result = []
      
      for i in dic:
        for j in dic:
          pick = (i + j) * -1
          if pick in dic: # 두 값을 더한 것에서 x -1 한 값이 있으면
            if i == j and j == pick and dic[i] < 3: # 다 같은데 개수가 안맞는 경우
              continue
            
            if i == j and j != pick and dic[i] < 2:
              continue
            
            if j == pick and i != j and dic[j] < 2:
              continue
            
            if i == pick and i != j and dic[i] < 2:
              continue
            
            sorted_arr = sorted([i, j, pick])
            if tuple(sorted_arr) not in s:
              result.append(sorted_arr)
              s.add(tuple(sorted_arr))

        
      return result