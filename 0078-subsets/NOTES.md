​# 풀이
- Difficulty:  Medium
- Topic:  Backtracking
- Elapsed Time:  10m
- Status:  O (2 times)
- Memo: 지난번엔 combinations 써서풀었는데 이번에는 백트래킹으로 품. 백트래킹 여러번 풀어서 감을 익혀야할듯

## 내 풀이
처음 answer.append(curr) 해서 값을 더하는게 아니라 배열을 가리키는 주소값을 넣었는지 값이 상하게 처리되서 시간을 많이 날렸음. 
```py
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def backtracking(curr: List[int], idx: int):
            # 현재 상태를 결과에 추가 (깊은 복사 사용)
            answer.append(curr[:])

            # idx부터 시작해서 모든 원소를 탐색
            for i in range(idx, len(nums)):
                curr.append(nums[i])  # 현재 원소를 추가
                backtracking(curr, i + 1)  # 다음 단계로 재귀 호출
                curr.pop()  # 백트래킹: 상태 복원

        backtracking([], 0)
        return answer
```

## 다른 풀이
### Approach 1: Cascading
1. [], [1]
2. [], [1], [2], [1,2]
3. [], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]
이런식으로 반복됨
```py
class Solution:
    def subsets(self, nums):
        # 부분 집합을 저장할 리스트 초기화 (초기에는 빈 집합만 포함)
        output = [[]]

        # 입력 리스트의 각 숫자에 대해 반복
        for num in nums:
            newSubsets = []  # 새로운 부분 집합을 저장할 리스트

            # 현재까지 만들어진 부분 집합에 대해 반복
            for curr in output:
                temp = curr.copy()  # 기존 부분 집합을 복사
                temp.append(num)  # 복사본에 현재 숫자를 추가
                newSubsets.append(temp)  # 새로운 부분 집합에 추가

            # 새로 만든 부분 집합들을 기존 결과에 병합
            for curr in newSubsets:
                output.append(curr)

        # 모든 부분 집합 반환
        return output

```

### Approach 2: Backtracking
백트래킹 코드이다. 내 코드랑 조금 다르다
```py
class Solution:
    def subsets(self, nums):
        self.output = []  # 모든 부분집합을 저장할 리스트
        self.n, self.k = len(nums), None  # n: 입력 배열의 길이, k: 현재 생성 중인 부분집합의 크기
        for self.k in range(self.n + 1):  # 0부터 n까지의 모든 크기의 부분집합 생성
            self.backtrack(0, [], nums)  # 백트래킹 함수 호출
        return self.output  # 모든 부분집합 반환

    def backtrack(self, first, curr, nums):
        if len(curr) == self.k:  # 현재 부분집합의 크기가 목표 크기(k)와 같으면
            self.output.append(curr[:])  # 현재 부분집합의 복사본을 결과에 추가
        for i in range(first, self.n):  # first부터 n-1까지 반복
            curr.append(nums[i])  # 현재 원소를 부분집합에 추가
            self.backtrack(i + 1, curr, nums)  # 다음 원소부터 재귀적으로 백트래킹
            curr.pop()  # 백트래킹: 추가했던 원소 제거

```

### Approach 3:
```py
```

### Approach 4:
```py
```

### Approach 5:
```py
```