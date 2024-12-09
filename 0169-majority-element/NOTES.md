# 풀이
- Difficulty:  Easy
- Topic:  Array / String
- Elapsed Time:  6m
- Status:  O
- Memo: 문제 자체는 정말 쉬운데 `follow up` 에 나온 linear time + O(1) space complexity 로 풀어보라는 것에 고민하다가 그냥 내가 아는 방법으로 풀었다.

## 내 풀이
단순하게 풀었다.
```py
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = defaultdict(int)
        n = len(nums)
        max_appear_time = n / 2

        for num in nums:
            dict[num] += 1
            if dict[num] >= max_appear_time:
                return num

```

## 다른 풀이
다른 여러 풀이방법은 생략했다. 다음 코드는 `Boyer-Moore Voting Algorithm`을 사용하여 majority element (과반수 이상 등장하는 원소)를 찾는 효율적인 방법이다. 이 알고리즘은 시간복잡도가 O(n), 공간복잡도가 O(1) 로 매우 효율적인 코드다.

### Approach 7: Boyer-Moore Voting Algorithm
```py
class Solution:
    def majorityElement(self, nums):
        count = 0  # 현재 후보 원소에 대해 유지되는 카운터
        candidate = None  # 현재 다수 원소로 가정하는 후보 값

        for num in nums:
          # 만약 count가 0이면, candidate를 num으로 업데이트
            if count == 0:
                candidate = num
            # num이랑 candidate 랑 같으면 count를 +1, 아니면 -1
            count += 1 if num == candidate else -1

        return candidate
```