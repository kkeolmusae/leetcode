# 풀이
- Difficulty:  Easy
- Topic:  Array / String
- Elapsed Time:  10m
- Status:  O
- Memo: 이전에 removeDuplicates Medium 버전으로 풀던거 생각해서 효율적으로 풀려고 하다보니 시간 많이 잡아먹음

## 내 풀이
```py
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1  # 현재 확인 중인 위치를 나타내는 포인터
        j = 1  # 중복이 제거된 배열을 저장할 위치를 나타내는 포인터

        while i < len(nums):  # 배열의 끝까지 확인
            if nums[i] == nums[i - 1]:  # 현재 숫자가 이전 숫자와 같다면
                i += 1  # 중복이므로 i만 증가시켜 다음 숫자로 이동
                continue  # 이후 로직을 건너뛰고 다음 반복으로 넘어감
            nums[j] = nums[i]  # 중복이 아니라면 현재 숫자를 위치 j에 저장
            i += 1  # 다음 숫자로 이동
            j += 1  # 중복이 제거된 배열의 다음 위치로 이동
        return j  # 중복이 제거된 배열의 길이를 반환

```

## 다른 풀이
### Approach 1: Two indexes approach
```py
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)  # 배열의 길이를 저장
        insertIndex = 1  # 중복이 제거된 숫자를 저장할 위치를 나타내는 변수

        for i in range(1, size):  # 배열의 두 번째 요소부터 끝까지 반복
            # 새로운 고유한 요소를 찾은 경우
            if nums[i - 1] != nums[i]:
                # 고유한 요소를 insertIndex 위치에 저장
                nums[insertIndex] = nums[i]
                # insertIndex를 1 증가시켜 다음 위치로 이동
                insertIndex = insertIndex + 1

        return insertIndex  # 중복이 제거된 배열의 길이를 반환

```
