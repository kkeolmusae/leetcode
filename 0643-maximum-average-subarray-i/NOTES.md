# 풀이

- LeetCode 75, Easy
- Sliding Window
- Time: 6m 53s
- 대충 풀었다가 시간초과 발생함. 그래도 풀긴함


## 내 풀이
- 처음엔 lidx, ridx 해서 sum(arr[lidx:ridx+1])/4 했는데 시간초가 발생했고,
- 두번째 수정했을때는 deque 에 넣었다 뺐다 하면서 sum(q)/4 했는데 또 시간초과 발생해서
- sum 연산이 오래걸리겠다고 생각해서 이전 값을 저장했다가 더하고 빼는 방식으로 갱신해서 문제 해결함
```py
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = -math.inf

        q = deque()  # deque 만들고
        prev = 0  # 배열의 sum 연산 대신 단순 +-를 하기 위해 이전 값 저장해둠
        for idx in range(len(nums)):
            q.append(nums[idx])  # 일단 prev에 더하고
            prev += nums[idx]

            if len(q) > k:
                prev -= q.popleft()  # 만약 k보다 사이즈 커지면 값 pop

            if len(q) == k:
                result = max(result, prev / k)
        return result
```

## 다른 풀이
### Approach #1 Cumulative Sum [Accepted]
배열을 nums 길이만큼 쓰는게 불필요하다고 생각되는 코드..
```py
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 누적 합 배열 생성
        sum_arr = [0] * len(nums)
        sum_arr[0] = nums[0]
        
        for i in range(1, len(nums)):
            sum_arr[i] = sum_arr[i - 1] + nums[i]
        
        # 첫 번째 k개의 요소의 평균 계산
        res = sum_arr[k - 1] * 1.0 / k
        
        # 슬라이딩 윈도우를 사용하여 최대 평균 찾기
        for i in range(k, len(nums)):
            res = max(res, (sum_arr[i] - sum_arr[i - k]) * 1.0 / k)
        
        return res
```

### Approach #2 Sliding Window [Accepted]
deque 안쓰고 해결함. 이게 정석인듯. 왜 나는 q를 사용했을까..
```py
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 처음 k개의 요소의 합 계산
        sum_val = sum(nums[:k])
        res = sum_val
        
        # 슬라이딩 윈도우를 사용하여 최대 합 계산
        for i in range(k, len(nums)):
            sum_val += nums[i] - nums[i - k]
            res = max(res, sum_val)
        
        # 최대 평균 반환
        return res / k
```