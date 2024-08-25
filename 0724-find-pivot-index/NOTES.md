# 풀이
- LeetCode 75, Easy
- Prefix Sum
- Time: 5m
- Prefix Sum의 유형은 어떻게 접근을 해야할지 감이 안잡혀서 처음에 고민을 좀 했음. 정석인지는 모르겠지만 쉽게 풀긴 함

## 내 풀이
왼쪽을 시작으로 pivot 계산하고, 오른쪽을 시작으로 pivot을 계산한 다음에 두 배열을 비교해서 같은 값이 있으면 리턴하고 없으면 -1 리턴하는 방법으로 품
```py
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        l_prev = [0] * n
        for i in range(1, len(nums)):  # 왼쪽부터 pivot 계산
            l_prev[i] = l_prev[i - 1] + nums[i - 1]

        r_prev = [0] * n
        for i in range(len(nums) - 2, -1, -1):  # 오른쪽부터 pivot 계산
            r_prev[i] = r_prev[i + 1] + nums[i + 1]

        for idx in range(n):  # 양쪽 비교해서 값이 같으면 idx 리턴
            if l_prev[idx] == r_prev[idx]:
                return idx
        return -1
```

## 다른 풀이
### Approach #1: Prefix Sum [Accepted]
나는 for문을 총 3번 돌아서 해결했는데, 이거는 sum 한번이랑 for문 한번으로 해결함
```py
class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)  # 배열 전체 요소의 합
        leftsum = 0  # 왼쪽 부분의 합을 저장할 변수

        for i, x in enumerate(nums):
            # 왼쪽 합이 전체 합에서 현재 값과 오른쪽 합을 뺀 값과 같다면 피벗 인덱스를 반환
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x  # 왼쪽 합에 현재 값을 더함
        
        return -1  # 피벗 인덱스를 찾지 못한 경우 -1 반환

```