# 풀이
- LeetCode 75, Medium
- Binary Search
- Time: 3m
- 오랜만에 LeetCode 75중에 아무거나 골라서 푸는데 걍 쉬웠음 

## 내 풀이
걍 현재위치의 값이 다음위치보다 크면 peak라서 idx 리턴함
```py
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for idx in range(len(nums) - 1):
            if nums[idx] > nums[idx + 1]:
                return idx

        return len(nums) - 1
```

## 다른 풀이
### Approach 1: Recursive Binary Search
```py
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 리스트 nums에서 피크 엘리먼트의 인덱스를 찾기 위해 search 함수를 호출
        return self.search(nums, 0, len(nums) - 1)

    def search(self, nums: List[int], l: int, r: int) -> int:
        # 시작점과 끝점이 같으면, 그것이 피크 엘리먼트의 위치임
        if l == r:
            return l
        
        # 중간 위치를 계산
        mid = (l + r) // 2
        
        # 중간 값이 오른쪽 이웃 값보다 크면, 왼쪽 구간에 피크가 있음
        if nums[mid] > nums[mid + 1]:
            return self.search(nums, l, mid)
        
        # 그렇지 않으면, 오른쪽 구간에 피크가 있음
        return self.search(nums, mid + 1, r)

```

### Approach 2: Iterative Binary Search
```py
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 리스트에서 탐색할 왼쪽(l)과 오른쪽(r) 인덱스 설정
        l = 0
        r = len(nums) - 1
        
        # 두 포인터가 만날 때까지 반복
        while l < r:
            # 중간값(mid) 계산
            mid = (l + r) // 2
            
            # mid 값이 mid+1 값보다 크면, 피크가 왼쪽에 존재
            if nums[mid] > nums[mid + 1]:
                r = mid  # 오른쪽 포인터를 중간으로 이동하여 왼쪽 부분 탐색
            else:
                l = mid + 1  # 왼쪽 포인터를 mid + 1로 이동하여 오른쪽 부분 탐색
        
        # 왼쪽 포인터가 최종적으로 가리키는 값이 피크 엘리먼트의 인덱스
        return l
```