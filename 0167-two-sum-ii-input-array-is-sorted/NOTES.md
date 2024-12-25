# 풀이
- Difficulty:  Medium
- Topic:  Two Pointers
- Elapsed Time:  7m
- Status:  O (2 times)
- Memo: 별로 안어려웠음.

## 내 풀이
```py
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lidx = 0
        ridx = len(numbers) - 1

        while True:
            x = numbers[lidx]
            y = numbers[ridx]

            if x + y == target:  # 숫자가 target이랑 같으면 끝
                return [lidx + 1, ridx + 1]

            if x + y > target:
                # 숫자 합친게 target 보다 크면 오른쪽 인덱스를 왼쪽으로 이동
                ridx -= 1
            else:
                # 숫자 합친게 target 보다 작으면 왼쪽 인덱스를 오른쪽으로 이동
                lidx += 1
```

## 다른 풀이
### Approach 1: Two Pointers
내 코드랑 아주 정말 비슷함
```py
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while low < high:
            sum = numbers[low] + numbers[high]

            if sum == target:
                return [low + 1, high + 1]
            elif sum < target:
                low += 1
            else:
                high -= 1
        return [-1, -1]
```