# 풀이
## 내 풀이
그냥 문제 그대로 nums1 에 nums2를 합치고 sort 했다. 
- 시간복잡도: O((n+m)log(n+m))
```py
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for idx in range(n):
            nums1[idx + m] = nums2[idx]
        
        nums1.sort()    
``` 

## 다른 풀이
### Three Pointers (Start From the Beginning)
- 시간복잡도: O(n+m)
```py
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # m 만큼 nums1 에서 추출
        nums1_copy = nums1[:m]

        # nums1Copy 및 nums2에 대한 포인터
        p1 = 0
        p2 = 0

        # nums1Copy랑 num2를 읽어서 더작은걸 nums1 에 넣음
        for p in range(n + m):
            # p1과 p2가 경계를 넘으면 안됨
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
```

### Three Pointers (Start From the End)
앞에 방식이랑 반대로 풀이
```py
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1 = m - 1
        p2 = n - 1

        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
```