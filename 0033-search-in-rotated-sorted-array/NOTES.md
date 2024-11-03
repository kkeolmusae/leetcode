# 풀이
- Medium
- Array / String
- Time: 20s
- 라이브러리로 그냥 품..

## 내 풀이
코드 그대로 target이 nums 에 있으면 index를 리턴하고 아니면 -1
```py
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1
```

## 다른 풀이
### Approach 1: Find Pivot Index + Binary Search
left: 배열에서 가장 작은 값의 위치, right: 배열에서 가장 큰 값의 위치
```py
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        # 회전된 배열에서 피벗 요소(가장 작은 요소)의 인덱스를 찾습니다.
        while left <= right:
            mid = (left + right) // 2
            # 중간 요소가 배열의 마지막 요소보다 크다면, 최소값은 오른쪽에 있습니다.
            if nums[mid] > nums[-1]:
                left = mid + 1
            # 중간 요소가 배열의 마지막 요소보다 작다면, 최소값은 왼쪽에 있습니다.
            else:
                right = mid - 1

        # 이진 탐색을 수행하는 함수 (left_boundary ~ right_boundary 범위 내)
        def binarySearch(left_boundary, right_boundary, target):
            left, right = left_boundary, right_boundary
            while left <= right:
                mid = (left + right) // 2
                # 중간 요소가 목표값과 같다면 인덱스를 반환합니다.
                if nums[mid] == target:
                    return mid
                # 중간 요소가 목표값보다 크다면, 왼쪽 부분을 탐색합니다.
                elif nums[mid] > target:
                    right = mid - 1
                # 중간 요소가 목표값보다 작다면, 오른쪽 부분을 탐색합니다.
                else:
                    left = mid + 1
            # 목표값을 찾지 못한 경우 -1을 반환합니다.
            return -1

        # 피벗 요소의 왼쪽 부분에서 이진 탐색을 수행합니다.
        if (answer := binarySearch(0, left - 1, target)) != -1:
            return answer

        # 피벗 요소의 오른쪽 부분에서 이진 탐색을 수행합니다.
        return binarySearch(left, n - 1, target)

```

### Approach 2: Find Pivot Index + Binary Search with Shift
```py
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        # 회전된 배열에서 피벗 요소(가장 작은 요소)의 인덱스를 찾습니다.
        while left <= right:
            mid = (left + right) // 2
            # 중간 요소가 배열의 마지막 요소보다 크다면, 최소값은 오른쪽에 있습니다.
            if nums[mid] > nums[-1]:
                left = mid + 1
            # 중간 요소가 배열의 마지막 요소보다 작다면, 최소값은 왼쪽에 있습니다.
            else:
                right = mid - 1

        # 피벗 요소의 인덱스를 0으로 하여 배열을 회전한 것처럼 이진 탐색을 수행합니다.
        def shiftedBinarySearch(pivot_index, target):
            # 배열을 피벗을 기준으로 회전한 상태에서 탐색할 수 있도록 shift를 설정합니다.
            shift = n - pivot_index
            # 탐색 범위를 피벗을 기준으로 설정합니다.
            left, right = (pivot_index + shift) % n, (pivot_index - 1 + shift) % n

            # 일반 이진 탐색과 유사하게 탐색을 수행합니다.
            while left <= right:
                mid = (left + right) // 2
                # mid 위치에서 shift를 제거하여 원래 배열의 인덱스를 맞춥니다.
                if nums[(mid - shift) % n] == target:
                    return (mid - shift) % n
                # 목표값이 현재 값보다 작으면 왼쪽으로 범위를 좁힙니다.
                elif nums[(mid - shift) % n] > target:
                    right = mid - 1
                # 목표값이 현재 값보다 크면 오른쪽으로 범위를 좁힙니다.
                else:
                    left = mid + 1
            # 목표값을 찾지 못한 경우 -1을 반환합니다.
            return -1

        # 피벗을 기준으로 회전한 배열에서 목표값을 이진 탐색으로 찾습니다.
        return shiftedBinarySearch(left, target)

```

### Approach 3: One Binary Search
```py
```