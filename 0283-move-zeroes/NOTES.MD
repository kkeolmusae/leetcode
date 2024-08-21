# 풀이
- LeetCode 75, Easy
- Two Pointers
- Time: 9m
- 문제 자체는 쉬웠는데 머리가 좀 안돌아갔음. two pointer 유형을 많이 안풀어서 그런듯

## 내 풀이
0 이랑 0 이 아닌 수를 찾아서 스왑. 대신 0이 왼쪽에 있는 경우에만 스왑
```py
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0

        while j < len(nums):
            while i < len(nums) and nums[i] != 0:  # i는 0을 찾아다니고
                i += 1

            while j < len(nums) and nums[j] == 0:  # j는 0 아닌걸 찾아다니고
                j += 1

            if j >= len(nums) or i >= len(nums):  # i 랑 j 중에 범위 벗어나면 끝
                break

            # 0이 왼쪽에 있고, 0이 아닌 숫자가 오른쪽에 있는 경우에만 바꾸자.
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1  # 0 이 오른쪽에 있고 0이 아닌 숫자가 왼쪽에 있으면 바꿀 필요없으니깐 j 만 이동
        return nums
```

## 다른 풀이
### Approach #1 (Space Sub-Optimal) [Accepted]
문제 조건이 `that you must do this in-place without making a copy of the array.` 인데... 이거 그냥 새로 배열 만든다음에 기존 nums에 덮어 쓰는거라 조건이 좀 안맞는듯함
```py
def moveZeroes(nums):
    n = len(nums)

    # 0의 개수를 센다.
    numZeroes = 0
    for i in range(n):
        numZeroes += (nums[i] == 0)

    # 0이 아닌 원소들이 원래 순서를 유지하도록 한다.
    ans = []
    for i in range(n):
        if nums[i] != 0:
            ans.append(nums[i])

    # 모든 0을 끝으로 이동시킨다.
    while numZeroes > 0:
        ans.append(0)
        numZeroes -= 1

    # 결과를 결합한다.
    for i in range(n):
        nums[i] = ans[i]
```

### Approach #2 (Space Optimal, Operation Sub-Optimal) [Accepted]
이거 좀 간단한듯. 순서대로 보면서 0이 아니면 앞에 순서대로 덮어쓰고, 끝까지 다 처리하고 나면 뒷쪽을 다 0으로 바꿈
```py
def moveZeroes(nums):
    lastNonZeroFoundAt = 0
    
    # 현재 요소가 0이 아닌 경우, 마지막으로 발견된 0이 아닌 요소 바로 앞에 위치시킵니다.
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[lastNonZeroFoundAt] = nums[i]
            lastNonZeroFoundAt += 1
    
    # 새로운 요소 처리가 끝난 후에는, 0이 아닌 모든 요소가 배열의 앞부분에 위치하게 됩니다.
    # 남은 배열의 모든 위치를 0으로 채워줍니다.
    for i in range(lastNonZeroFoundAt, len(nums)):
        nums[i] = 0
```

### Approach #3 (Optimal) [Accepted]
위에 코드를 리팩토링한거. 내가 딱 이렇게 하고싶었음..
```py
def moveZeroes(nums):
    lastNonZeroFoundAt = 0
    
    # 배열을 순회하며, 현재 요소가 0이 아닌 경우, 마지막으로 발견된 0이 아닌 요소와 교체합니다.
    for cur in range(len(nums)):
        if nums[cur] != 0:
            nums[lastNonZeroFoundAt], nums[cur] = nums[cur], nums[lastNonZeroFoundAt]
            lastNonZeroFoundAt += 1
```