# 풀이 
## 내 풀이. 
- 시간복잡도: O(nlogn + n + m^2)
```py
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      dic = {}
      nums.sort() # O(nlogn)
      
      for num in nums: # 같은 숫자라 여러개 있을 수 있어서 숫자별로 개수를 저장함 O(n)
        if num not in dic: 
          dic[num] = 1
        else:
          dic[num] += 1
      
      s = set() # 중복된 조합을 방지하기 위함
      result = []
      
      # O(m^2)
      for i in dic:
        for j in dic:
          pick = (i + j) * -1
          if pick in dic: # 두 값을 더하고 -1을 곱한 값이 dic에 있으면 => 세 숫자를 더했을떄 0 임
            if i == j and j == pick and dic[i] < 3: # 다 같은데 개수가 안맞는 경우
              continue
            
            if i == j and j != pick and dic[i] < 2: # i == j != pick 이면 2개가 있어야함
              continue
            
            if j == pick and i != j and dic[j] < 2: # i != j == pick 이면 2개가 있어야함
              continue
            
            if i == pick and i != j and dic[i] < 2: # i == pick != j 이면 2개가 있어야함
              continue
            
            sorted_arr = sorted([i, j, pick])
            if tuple(sorted_arr) not in s:
              result.append(sorted_arr)
              s.add(tuple(sorted_arr))

        
      return result
```

## 다른 풀이

### Two Pointer
- 시간 복잡도: 
```py
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # 정렬
        for i in range(len(nums)):
            if nums[i] > 0: # 제일 작은게 0 보다 크면 정답이 나올 수 없음
                break
            if i == 0 or nums[i - 1] != nums[i]: # 이전 수와 같은 수가 반복되는 경우(즉, nums[i] == nums[i - 1]), 중복된 결과를 피하기 위해 넘어갑니다.
                self.twoSumII(nums, i, res)
        return res

    # threeSum 메서드에서 주어진 인덱스 i 이후의 배열 부분에서 두 수를 찾아 세 수의 합이 0이 되도록 함 (투 포인터 사용)
    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
```

### Hashset
```py
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    # threeSum 메서드에서 선택된 첫 번째 숫자 nums[i]에 대해, 두 번째와 세 번째 숫자를 찾음. 두 수의 합이 특정 값이 되는지를 seen 집합을 이용하여 확인함
    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1
```

### No Sort
```py
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res: 결과를 저장할 집합입니다. 세 숫자의 조합이 중복되지 않도록 집합을 사용하여 중복된 조합이 자동으로 제거됩니다.
        # dups: 이미 처리된 첫 번째 숫자 val1을 기록하는 집합입니다. 이를 통해 중복된 첫 번째 숫자로 인해 발생하는 중복된 조합을 피할 수 있습니다.
        # seen: val2의 값을 키로, 그 값이 발견된 val1의 인덱스 i를 값으로 저장하는 사전입니다. 이는 complement를 찾을 때 val1이 동일한지 확인하는 데 사용됩니다.

        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i + 1 :]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res
```