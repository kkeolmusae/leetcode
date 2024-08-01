# 풀이
## 내 풀이
count 가 2 보다 크면 숫자가 3번중복된거라 그 index를 del 하는 방법으로 풀었음. 
- 시간복잡도: O(n^2)
```py
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        count = 1
        n = len(nums)

        while idx < n:
            if nums[idx] == nums[idx - 1]:
                count += 1

                if count > 2:
                    del nums[idx]
                    idx -= 1
                    n -= 1
            else:
                count = 1
            idx += 1
        return nums​
```

## 다른 풀이
### 원하지 않는 복제 덮어쓰기
리스트 nums에서 최대 두 번까지의 중복을 허용하며 중복된 요소를 제거하는 함수.
처음 코드 봤을때 이해 잘 못함.
- 시간복잡도: O(n)
```py
class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:

        j, count = 1, 1

        for i in range(1, len(nums)):

            # 현재 요소 nums[i]와 이전 요소 nums[i - 1]가 같으면 중복이므로 count를 증가시킵니다.

            if nums[i] == nums[i - 1]:
                count += 1
            else:
                # 현재 요소가 이전 요소와 다르면 다른 숫자가 나온 것이므로 count를 1로 초기화합니다.
                count = 1

            # if count <= 2: 현재 숫자가 두 번 이하로 나왔을 때만 해당 요소를 유지
            if count <= 2:
                nums[j] = nums[i] # 중복을 허용하는 최대 횟수까지 리스트에 남기기 위해 현재 숫자를 j 위치에 저장합니다.
                j += 1 # 다음으로 채울 위치를 가리키는 인덱스를 증가시킵니다.


        return j
```