​# 풀이
- Difficulty:  Medium
- Topic:  Array / String
- Elapsed Time:  6m?
- Status:  O (2 times)
- Memo: 이전에 풀었던 문제인데 복기도 안되어있고, 코드도 좀 익숙치 않은 걸 보니 뭔가 보고 참고한듯한 느낌이었음. 근데 이번에는 혼자 품

## 내 풀이
앞에서 부터 최대 점프 가능한 위치를 갱신하면서 해결함.
```py
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # nums 길이가 1이면 가능
        if len(nums) == 1:
            return True

        # nums의 첫번째값이 0이면 False (nums 길이가 2이상임)
        if nums[0] == 0:
            return False

        last_idx = len(nums) - 1  # 도달해야하는 지점
        curr = 0  # 현재 위치
        can_jump = nums[curr]  # 최대 점프 가능 위치

        while curr <= can_jump:
            can_jump = max(curr + nums[curr], can_jump)  # 최대 점프 가능 위치 갱신
            if can_jump >= last_idx:  # 점프 가능하면 True
                return True
            curr += 1  # 다음 발판으로
        return False  # last_idx에 도달 못한거니깐 False

```

## 다른 풀이
### Approach 1: Backtracking (Not Accepted: TLE)
백트래킹으로 푼 방법인데 제목 그대로 TLE 이다. 참고 정도만 하면 될 듯?
```py
class Solution:
    # 특정 위치에서 배열 끝까지 도달할 수 있는지 확인하는 재귀 함수
    def canJumpFromPosition(self, position, nums):
        # 현재 위치가 마지막 인덱스인 경우, 도달 가능
        if position == len(nums) - 1:
            return True
        
        # 현재 위치에서 가장 멀리 갈 수 있는 위치 계산
        furthestJump = min(position + nums[position], len(nums) - 1)
        
        # 현재 위치 다음부터 가장 멀리 갈 수 있는 위치까지 반복하며 탐색
        for nextPosition in range(position + 1, furthestJump + 1):
            # 재귀적으로 다음 위치에서 끝까지 도달 가능한지 확인
            if self.canJumpFromPosition(nextPosition, nums):
                return True  # 도달 가능하면 바로 True 반환
        
        # 어떤 위치에서도 끝에 도달하지 못한 경우 False 반환
        return False

    # 배열의 시작점(0번 인덱스)에서 끝까지 도달 가능한지 확인하는 함수
    def canJump(self, nums):
        return self.canJumpFromPosition(0, nums)

```

### Approach 2: Dynamic Programming Top-down
시간복잡도 O(n) 으로 해결하는 방법이다.
```py
class Solution:
    def __init__(self):
        # 메모이제이션 배열 초기화
        self.memo = []
        # 입력 배열을 저장할 변수
        self.nums = []

    # 특정 위치에서 끝까지 도달할 수 있는지 확인하는 재귀 함수
    def canJumpFromPosition(self, position):
        # 메모이제이션 확인: 이미 계산된 위치라면 결과 반환
        if self.memo[position] != -1:
            return self.memo[position] == 1  # 1은 도달 가능, 0은 도달 불가
        
        # 현재 위치에서 가장 멀리 갈 수 있는 위치 계산
        furthestJump = min(position + self.nums[position], len(self.nums) - 1)
        
        # 현재 위치 이후의 모든 가능한 점프 위치를 탐색
        for nextPosition in range(position + 1, furthestJump + 1):
            # 다음 위치에서 끝까지 도달 가능하면 메모이제이션에 기록 후 True 반환
            if self.canJumpFromPosition(nextPosition):
                self.memo[position] = 1
                return True
        
        # 끝까지 도달 불가능한 경우 메모이제이션에 기록 후 False 반환
        self.memo[position] = 0
        return False

    # 배열의 시작점에서 끝까지 도달 가능한지 확인하는 함수
    def canJump(self, nums):
        self.nums = nums  # 입력 배열 저장
        # 메모이제이션 배열 초기화: -1은 아직 방문하지 않은 상태
        self.memo = [-1] * len(nums)
        # 마지막 위치는 항상 도달 가능한 상태로 설정
        self.memo[-1] = 1
        # 시작점에서 끝까지 도달 가능한지 확인
        return self.canJumpFromPosition(0)

```

### Approach 3: Dynamic Programming Bottom-up
```py
class Solution(object):
    def canJump(self, nums):
        # 상태를 나타내는 상수: 도달 가능(GOOD), 도달 불가능(BAD), 미확인(UNKNOWN)
        GOOD, BAD, UNKNOWN = 1, 0, -1
        
        # 메모이제이션 배열 초기화: UNKNOWN으로 채우고 마지막 위치는 GOOD
        memo = [UNKNOWN] * len(nums)
        memo[-1] = GOOD  # 마지막 위치는 항상 도달 가능하므로 GOOD으로 설정
        
        # 뒤에서부터 거꾸로 탐색하며 메모이제이션 배열 업데이트
        for i in range(len(nums) - 2, -1, -1):  # 마지막 이전 위치부터 탐색
            # 현재 위치에서 가장 멀리 점프할 수 있는 위치 계산
            furthest_jump = min(i + nums[i], len(nums) - 1)
            
            # 현재 위치에서 점프 가능한 모든 위치 탐색
            for j in range(i + 1, furthest_jump + 1):
                # 점프한 위치가 GOOD인 경우, 현재 위치도 GOOD으로 설정
                if memo[j] == GOOD:
                    memo[i] = GOOD
                    break  # 더 이상 탐색할 필요 없음
        
        # 시작점(0번 인덱스)이 GOOD인지 확인하여 결과 반환
        return memo[0] == GOOD

```

### Approach 4: Greedy
처음 풀려있었던 방식
```py
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 마지막으로 도달 가능한 위치를 저장 (초기값: 배열의 끝)
        lastPos = len(nums) - 1
        
        # 배열을 거꾸로 순회
        for i in range(len(nums) - 1, -1, -1):
            # 현재 위치에서 마지막 도달 가능한 위치에 도달할 수 있으면
            if i + nums[i] >= lastPos:
                # 마지막 도달 가능한 위치를 현재 위치로 갱신
                lastPos = i
        
        # 마지막 도달 가능한 위치가 시작점(0번 인덱스)인지 확인
        return lastPos == 0
```