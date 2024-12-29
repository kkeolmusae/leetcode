# 풀이
- Difficulty:  Medium
- Topic:  Sliding Window
- Elapsed Time:  13m
- Status:  O 
- Memo: 구현 방향은 금방 생각해냈는데 효율적으로 하지 못해서 시간이 좀 더 걸림

## 내 풀이
- 처음시도: TLE(time limit exceeded) 
- 개선 1: SUM(sub_array) 를 미리 계산하여 2206ms 로 단축함
- 개선 2: LEN(sub_array) 를 미리 계산하여 31ms으로 단축함
```py
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # nums 길이가 1일때
        if len(nums) == 1:
            return 1 if nums[0] >= target else 0
        lidx = 0
        ridx = 0
        result = math.inf
        total = nums[0]
        sub_array_len = 1

        while ridx < len(nums) and lidx < len(nums):
            if total >= target:
                result = min(sub_array_len, result)
                if lidx <= ridx:
                    total -= nums[lidx]
                    sub_array_len -= 1
                    lidx += 1
                else:
                    ridx += 1
                    total += nums[ridx] if ridx < len(nums) else 0
                    sub_array_len += 1 if ridx < len(nums) else 0
            elif total < target:
                ridx += 1
                total += nums[ridx] if ridx < len(nums) else 0
                sub_array_len += 1 if ridx < len(nums) else 0

        return result if result != math.inf else 0
```

## 다른 풀이
### Approach: Sliding Window
내가 변수를 비효율적으로 사용했구나 라는 반성을 하게 됨. 조금 더 생각하면서 풀었으면 더 쉽게 풀렸을 듯?
```py
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0  # 윈도우의 왼쪽 포인터
        right = 0  # 윈도우의 오른쪽 포인터
        sumOfCurrentWindow = 0  # 현재 윈도우의 합
        res = float('inf')  # 결과값, 최소 길이를 저장하며 초기값은 무한대로 설정

        # 오른쪽 포인터를 이동하며 배열을 순회
        for right in range(0, len(nums)):
            sumOfCurrentWindow += nums[right]  # 현재 윈도우에 새로운 값을 추가

            # 현재 윈도우의 합이 target 이상일 경우
            while sumOfCurrentWindow >= target:
                # 최소 길이를 갱신
                res = min(res, right - left + 1)
                # 윈도우의 왼쪽 값을 제거하여 윈도우 크기를 줄임
                sumOfCurrentWindow -= nums[left]
                left += 1

        # 최소 길이가 갱신되지 않았다면(조건을 만족하는 윈도우가 없는 경우) 0 반환
        return res if res != float('inf') else 0
```
