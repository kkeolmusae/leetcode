# 풀이
- LeetCode 75, medium
- Array / String
- Time: 못품 (>= 20m)
- 코드 자체는 단순한데 이런 방법을 생각해내는게 쉽지 않을듯. 

## 다른 풀이
first_num 보다 작거나 같으면 업데이트, first_num보다는 크고 second_num 보다 작거나 같으면 업데이트, first_num이랑 second_num보다 크면 True를 리턴하는 방식임. 코드보고 생각해보니 이해가 됨
```py
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = math.inf
        second_num = math.inf

        for num in nums:
            if num <= first_num:  # first_num 배치하고
                first_num = num
            elif num <= second_num:
                # first_num 보다 크고 second_num보다 작으면 second_num 배치
                second_num = num
            else:
                # first_num이랑 second_num 보다 크면 조건 중족시킨거니깐
                return True

        return False
```