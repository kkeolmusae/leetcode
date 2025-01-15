# 풀이
- Difficulty:  Medium
- Topic:  Backtracking
- Elapsed Time:  10m
- Status:  O
- Memo:  풀긴 풀었는데 전날에 이해못해서 해설보고 이해한 다음에 다시 푼거라 풀었다고 해도 될지 의문이다.

## 내 풀이
이게... backtracking 이 맞나? 싶기도하고... dfs 아닌가 싶은 느낌..
```py
class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        result = []

        # 문자열이 길이 1인 경우
        if len(s) == 1:
            return [[s]]

        def backtracking(curr: List[str], s: str):

            if len(s) == 0:
                result.append(curr)
                return

            for idx in range(1, len(s) + 1):
                if self.isPalindrome(s[:idx]):  # 팰린드롬이면
                    # 팰린드롬인 부분은 curr에 추가하고, 나머지는 다음으로
                    backtracking(curr + [s[:idx]], s[idx:])

        backtracking([], s)
        return result
```

## 다른 풀이
### Approach 1: Backtracking
```py
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 결과를 저장할 리스트
        result = []
        # DFS를 시작하여 문자열 분할 탐색
        self.dfs(s, [], result)
        return result

    # 주어진 문자열이 팰린드롬인지 확인하는 함수
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]  # 문자열을 뒤집은 결과와 원래 문자열을 비교하여 팰린드롬 여부 확인

    # 깊이 우선 탐색(DFS)을 사용한 분할 탐색
    def dfs(self, s: str, path: List[str], result: List[List[str]]):
        # 종료 조건: 남은 문자열이 없으면 현재 경로를 결과 리스트에 추가
        if not s:
            result.append(path)
            return

        # 가능한 모든 분할 위치에 대해 반복
        for i in range(1, len(s) + 1):
            # 현재 접두사(s[:i])가 팰린드롬인지 확인
            if self.isPalindrome(s[:i]):
                # 팰린드롬인 경우, 현재 경로(path)에 추가하고 재귀적으로 탐색
                self.dfs(s[i:], path + [s[:i]], result)  # 나머지 문자열(s[i:])로 탐색
                # path + [s[:i]]로 새로운 리스트를 만들어 재귀 호출 (기존 path는 불변)

```

### Approach 2: Backtracking with Dynamic Programming
이해못했지만 일단 가져와봤다!
```py
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        len_s = len(s)  # 문자열의 길이
        # DP 테이블 초기화: dp[i][j]는 s[i:j+1]이 팰린드롬인지 여부를 저장
        dp = [[False] * len_s for _ in range(len_s)]
        result = []  # 결과를 저장할 리스트
        # DFS 탐색 시작
        self.dfs(result, s, 0, [], dp)
        return result

    def dfs(
        self,
        result: List[List[str]],  # 결과 리스트
        s: str,                  # 입력 문자열
        start: int,              # 탐색 시작 인덱스
        currentList: List[str],  # 현재까지의 팰린드롬 분할 결과
        dp: List[List[bool]],    # DP 테이블
    ):
        # 종료 조건: 시작 인덱스가 문자열 길이 이상이면 현재 조합을 결과에 추가
        if start >= len(s):
            result.append(list(currentList))  # 현재 경로를 결과 리스트에 추가
            return

        # start부터 문자열 끝까지 반복하면서 팰린드롬 확인
        for end in range(start, len(s)):
            # s[start] == s[end]이고, 길이가 2 이하이거나 중간 부분이 팰린드롬이면
            if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                dp[start][end] = True  # dp[start][end]를 True로 설정
                currentList.append(s[start : end + 1])  # 현재 팰린드롬을 추가
                # end + 1부터 나머지 문자열에 대해 탐색
                self.dfs(result, s, end + 1, currentList, dp)
                currentList.pop()  # 백트래킹: 마지막 팰린드롬 제거
```
