# 풀이
- Difficulty:  Medium
- Topic:  Array / String
- Elapsed Time:  10m
- Status:  O 
- Approach:  -
- Memo:  지난번에 못풀었던 문제. 시간복잡도 O(n)으로 해결하는 방법을 고민하다가 시간 많이 씀

## 내 풀이 풀이
first_num 보다 작거나 같으면 업데이트, first_num보다는 크고 second_num 보다 작거나 같으면 업데이트, first_num이랑 second_num보다 크면 True를 리턴하는 방식임
```py
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = math.inf
        second = math.inf
        for curr in nums:
            if curr <= first:
                first = curr
            elif curr <= second:
                second = curr
            else:
                return True

        return False
```