# 풀이
- Difficulty:  Medium
- Topic:  Backtracking
- Elapsed Time:  5m
- Status:  O
- Memo: 0040 문제랑 0078 문제 풀고나서푸는거라 그런지 금방 풀었다. 근데 100% 이해하고 푼다기 보다는 대충 느낌으로 푸는듯....

## 내 풀이
```py
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        def backtracking(curr: List[int], startIdx: int):
            result.append(curr[:])

            for i in range(startIdx, n):
                if i > startIdx and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                backtracking(curr, i + 1)
                curr.pop()

        backtracking([], 0)
        return result
```

## 다른 풀이
### Approach 1: Cascading (Iterative)
```py
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()  # 중복 처리를 위해 입력 배열 정렬
        subsets = [[]]  # 빈 부분집합으로 시작
        subsetSize = 0  # 이전 단계의 부분집합 크기
        for i in range(len(nums)):
            # subsetSize는 이전 단계에서 생성된 부분집합의 크기를 나타냅니다.
            # 이 값은 또한 이번 단계에서 생성될 부분집합의 시작 인덱스를 나타냅니다.
            startingIndex = (
                subsetSize if i >= 1 and nums[i] == nums[i - 1] else 0
            )
            # 중복된 숫자의 경우, 이전 단계에서 새로 추가된 부분집합부터 시작
            # 중복되지 않은 숫자의 경우, 모든 기존 부분집합에 대해 새 부분집합 생성
            subsetSize = len(subsets)  # 현재 부분집합의 총 개수
            for j in range(startingIndex, subsetSize):
                currentSubset = list(subsets[j])  # 현재 부분집합 복사
                currentSubset.append(nums[i])  # 현재 숫자를 부분집합에 추가
                subsets.append(currentSubset)  # 새로운 부분집합을 결과에 추가
        return subsets  # 모든 부분집합 반환

```

### Approach 2: Backtracking
```py
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()  # 중복 처리를 위해 입력 배열 정렬
        subsets = []  # 모든 부분집합을 저장할 리스트
        currentSubset = []  # 현재 생성 중인 부분집합
        self.subsetsWithDupHelper(subsets, currentSubset, nums, 0)
        return subsets

    def subsetsWithDupHelper(self, subsets, currentSubset, nums, index):
        # 지금까지 형성된 부분집합을 subsets 리스트에 추가
        subsets.append(list(currentSubset))
        
        for i in range(index, len(nums)):
            # 현재 원소가 중복이면 건너뛰기
            if i != index and nums[i] == nums[i - 1]:
                continue
            currentSubset.append(nums[i])  # 현재 원소를 부분집합에 추가
            self.subsetsWithDupHelper(subsets, currentSubset, nums, i + 1)  # 재귀 호출
            currentSubset.pop()  # 백트래킹: 추가했던 원소 제거

```