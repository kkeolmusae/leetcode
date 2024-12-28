# 풀이
- Difficulty:  Medium
- Topic:  Two Pointers
- Elapsed Time:  13m
- Status:  O (2 times)
- Memo: 일단 풀긴 풀었는데.... Two Pointer 로 풀지 않았고 코드가 좀 비효율적인 듯 하다. 그래서 다른 풀이 보고 다시 풀었다. 제일 마지막으로 푼 방식대로 푸는 연습을 좀 해야할듯.

## 내 풀이
```py
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        # 가장 작은 숫자가 0 보다 크면 0을 만들 수 없기에 빈 배열 리턴
        if nums[0] > 0:
            return []

        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # 중복된 숫자는 건너뛰기
                continue
            self.twoSum(i, nums, result)

        return result

    def twoSum(
        self, i: int, nums: List[int], result: List[List[int]]
    ) -> List[List[int]]:
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                result.append([nums[i], nums[lo], nums[hi]])
                while lo < hi and nums[lo] == nums[lo + 1]:  # 중복된 숫자는 건너뛰기
                    lo += 1
                while lo < hi and nums[hi] == nums[hi - 1]:  # 중복된 숫자는 건너뛰기
                    hi -= 1
                lo += 1
                hi -= 1
```

## 다른 풀이

### Approach 1: Two Pointers
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

### Approach 2: Hashset
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

### Approach 3: "No-Sort"
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