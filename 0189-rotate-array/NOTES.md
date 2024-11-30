# 풀이
- Medium
- Array / String
- Time: 10m
- 추가 배열을 할당하지 않으면서 효율적으로 짜는 방법이 생각이 안나서 insert 로 해결하긴 했는데 시간 복잡도 측면에서 최악인듯하다. 

## 내 풀이
```py
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        for _ in range(k):
            nums.insert(0, nums.pop())

        return nums
```

## 다른 풀이
### Approach 1: Brute Force
```py
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # k가 리스트의 길이(len(nums)) 이상인 경우, 실제로 회전해야 하는 횟수는 k % len(nums)와 같다
        k %= len(nums)

        for i in range(k):
            # k 만큼 회적, 한 번의 회전은 리스트의 마지막 요소를 리스트의 시작으로 이동시킴
            previous = nums[-1]
            for j in range(len(nums)):
                # 리스트의 각 요소를 순회하며, 현재 요소를 이전 요소로 교체합니다.
                nums[j], previous = previous, nums[j]
```

### Approach 2: Using Extra Array
```py
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        a = [0] * n

        # 회전했을때의 위치에 배치하는데 임시배열 a를 사용함
        for i in range(n):
            a[(i + k) % n] = nums[i]

        # a를 nums로 복사
        nums[:] = a
```

### Approach 3: Using Cyclic Replacements
사이클 기반 회전(cyclic replacements)으로 해결. 이게 정석으로 푼 방법인듯
```py
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # 리스트의 길이
        n = len(nums)
        # k가 리스트 길이를 초과할 경우 최적화
        k %= n

        # 시작 인덱스와 처리한 요소 개수를 초기화
        start = count = 0

        # 모든 요소를 이동할 때까지 반복
        while count < n:
            # 현재 위치와 이전 값을 초기화
            current, prev = start, nums[start]

            # 사이클 처리
            while True:
                # 다음 인덱스를 계산
                next_idx = (current + k) % n
                # 다음 위치의 값을 저장하고 교체
                nums[next_idx], prev = prev, nums[next_idx]
                # 현재 위치를 다음 위치로 이동
                current = next_idx
                # 처리한 요소 개수를 증가
                count += 1

                # 사이클이 끝나면 종료
                if start == current:
                    break
            # 다음 사이클의 시작 인덱스로 이동
            start += 1

```
