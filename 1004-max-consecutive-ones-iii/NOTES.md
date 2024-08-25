# 풀이
- LeetCode 75, Medium
- Sliding Window
- Time: 18m
- Sliding Window 방식으로 해결하려고 했는데 방법이 안떠올라서 deque 로 해결함

## 내 풀이
```py
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        q = deque()
        result = 0

        if k == 0:  # k 가 0인 경우, 1이 나올때 마다 cnt++ 하고 0나오면 초기화 하는 방법으로 최대값 구하기
            cnt = 0
            for n in nums:
                if n == 1:
                    cnt += 1
                else:
                    cnt = 0
                result = max(result, cnt)
        else:
            #  k가 0이 아니면, q사용해서 q의 최대 길이를 구하기
            for n in nums:
                if n == 1:
                    q.append(n)
                else:
                    if k > 0:  # k가 있으면 0넣고
                        q.append(n)
                        k -= 1
                    else:  # k 없으면 처음에 넣었던 0 빼고 넣어야함
                        while q[0] != 0:
                            q.popleft()  # 1 날리고
                        q.popleft()  # 연결해주던 0 지우고
                        q.append(n)  # 새 0 넣고
                result = max(result, len(q))
        return result
```

## 다른 풀이

### Approach: Sliding Window
```py
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            # 현재 요소가 0이라면 k를 감소시킵니다.
            if nums[right] == 0:
                k -= 1
            
            # k가 음수가 되면 윈도우 내의 0의 개수가 허용된 범위를 초과한 것이므로
            # left를 이동시켜 윈도우를 줄입니다.
            if k < 0:
                # left가 가리키는 요소가 0이면 k를 증가시킵니다.
                if nums[left] == 0:
                    k += 1
                left += 1
        
        return right - left + 1
```