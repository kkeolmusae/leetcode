# 풀이
- LeetCode 75, Easy
- Hash Map / Set
- Time: 2m
- 파이썬이라 쉬움. 차집합 써서 해결함

## 내 풀이
```py
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        return [list(s1 - s2), list(s2 - s1)]
```

## 다른 풀이
파이썬이라서 쉽게 `set - set` 으로 해결했지만, 다른 언어였다면 for문 돌면서 처리했을 듯 하다.
### Approach 1: Brute Force
```py
class Solution:
    # 첫 번째 인자인 nums1에 존재하지만 두 번째 인자인 nums2에는 존재하지 않는 요소들을 반환
    def getElementsOnlyInFirstList(self, nums1, nums2):
        onlyInNums1 = set()

        # nums1 리스트의 각 요소를 순회
        for num in nums1:
            existInNums2 = False
            # num이 nums2에 존재하는지 확인
            for x in nums2:
                if x == num:
                    existInNums2 = True
                    break
            
            # nums2에 존재하지 않으면 onlyInNums1 집합에 추가
            if not existInNums2:
                onlyInNums1.add(num)
        
        # 리스트로 변환하여 반환
        return list(onlyInNums1)

    def findDifference(self, nums1, nums2):
        # nums1과 nums2에 대해 각각 getElementsOnlyInFirstList 함수를 호출하고 결과를 리스트로 반환
        return [self.getElementsOnlyInFirstList(nums1, nums2), self.getElementsOnlyInFirstList(nums2, nums1)]

```

### Approach 2: HashSet
```py
class Solution:
    # 첫 번째 인자인 nums1에 존재하지만 두 번째 인자인 nums2에는 존재하지 않는 요소들을 반환
    def getElementsOnlyInFirstList(self, nums1, nums2):
        onlyInNums1 = set()

        # nums2의 요소들을 집합으로 저장
        existsInNums2 = set(nums2)

        # nums1 리스트의 각 요소를 순회
        for num in nums1:
            if num not in existsInNums2:  # nums2에 존재하지 않으면 onlyInNums1 집합에 추가
                onlyInNums1.add(num)

        # 집합을 리스트로 변환하여 반환
        return list(onlyInNums1)

    def findDifference(self, nums1, nums2):
        # nums1과 nums2에 대해 각각 getElementsOnlyInFirstList 함수를 호출하고 결과를 리스트로 반환
        return [self.getElementsOnlyInFirstList(nums1, nums2), self.getElementsOnlyInFirstList(nums2, nums1)]

```