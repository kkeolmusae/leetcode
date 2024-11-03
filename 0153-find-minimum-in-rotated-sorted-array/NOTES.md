# 풀이
- Medium
- Array / String
- Time: 10s?
- 음 문제의도랑 다르게 푼 것 같은데 일단 아주 쉽게 품.

## 내 풀이
```py
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
```

## 다른 풀이
### Approach 1: Binary Search
가장 작은 숫자를 찾는건데 binary search 할 필요가 있나...
```py
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 리스트에 요소가 하나만 있다면, 그 요소를 반환합니다.
        if len(nums) == 1:
            return nums[0]

        # 왼쪽 포인터
        left = 0
        # 오른쪽 포인터
        right = len(nums) - 1

        # 배열의 마지막 요소가 첫 번째 요소보다 크면 회전이 없다는 뜻입니다.
        # 예: 1 < 2 < 3 < 4 < 5 < 7인 경우, 이미 정렬된 배열입니다.
        # 따라서 가장 작은 요소는 첫 번째 요소인 nums[0]입니다.
        if nums[right] > nums[0]:
            return nums[0]

        # 이진 탐색을 수행합니다.
        while right >= left:
            # 중간 요소를 찾습니다.
            mid = left + (right - left) // 2
            
            # 만약 중간 요소가 다음 요소보다 크다면, mid+1 요소가 가장 작은 요소입니다.
            # 이 지점이 값이 높은 곳에서 낮은 곳으로 바뀌는 지점입니다.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            # 만약 중간 요소가 이전 요소보다 작다면, mid 요소가 가장 작은 요소입니다.
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # 중간 요소가 첫 번째 요소보다 크다면, 가장 작은 값은 오른쪽에 있습니다.
            # 여전히 nums[0]보다 큰 요소들을 처리하고 있기 때문입니다.
            if nums[mid] > nums[0]:
                left = mid + 1
            # 첫 번째 요소가 중간 요소보다 크다면, 가장 작은 값은 왼쪽에 있습니다.
            else:
                right = mid - 1

```

### Approach 2:
```py
```

### Approach 3:
```py
```