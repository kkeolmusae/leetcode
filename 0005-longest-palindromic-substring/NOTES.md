# 풀이
- LeetCode 75, Medium
- DP
- Time: x
- dp 로 못풀어서 for문 중첩했는데 이것도 시간제한에 걸림. 해설보고 접근다르게 해서 for문 중첩으로 풀긴했는데 dp로는 아예 못품.

## 내 풀이
```py
class Solution:
    def checkPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        if n == 1:
            return s

        # 제일 긴 케이스 부터 짧은 케이스로 해야 시간초과 발생안함
        # 처음에 짧 -> 긴 순으로 해서 max인 케이스를 리턴하려고 하다보니 전체를 다 훑게되서 시간초과발생함
        for length in range(n, 0, -1):  # n길이부터 0까지 감소 (체크할 문자열의 길이)
            for idx in range(n - length + 1):
                # 발견하면 그게 긴거임
                if self.checkPalindrome(s, idx, idx + length - 1):
                    return s[idx : idx + length]
```

## 다른 풀이
### Approach 1: Check All Substrings
O(n^3) 으로 비효율적인 방식.
```py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start : start + length]

        return ""
```

### Approach 2: Dynamic Programming
```py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)  # 문자열의 길이를 저장
        dp = [[False] * n for _ in range(n)]  # n x n 크기의 2차원 배열 dp 초기화 (모든 값을 False로 설정)
        ans = [0, 0]  # 가장 긴 회문의 시작 및 끝 인덱스를 저장하는 리스트 초기화

        # 길이가 1인 부분 문자열 (모든 문자는 자신을 회문으로 가짐)
        for i in range(n):
            dp[i][i] = True  # dp[i][i]는 항상 True

        # 길이가 2인 부분 문자열 확인
        for i in range(n - 1):
            if s[i] == s[i + 1]:  # 두 문자가 같으면
                dp[i][i + 1] = True  # dp[i][i+1]을 True로 설정
                ans = [i, i + 1]  # 가장 긴 회문 인덱스 업데이트

        # 길이가 3 이상인 부분 문자열 확인
        for diff in range(2, n):  # diff는 현재 검사할 부분 문자열의 길이 - 1
            for i in range(n - diff):  # i는 시작 인덱스
                j = i + diff  # j는 끝 인덱스
                # 첫 번째와 마지막 문자가 같고, 내부 문자열이 회문인 경우
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True  # dp[i][j]를 True로 설정
                    ans = [i, j]  # 가장 긴 회문 인덱스 업데이트

        # 가장 긴 회문 부분 문자열 반환
        i, j = ans  # 가장 긴 회문 인덱스
        return s[i : j + 1]  # 인덱스를 이용해 회문 반환

```

### Approach 3: Expand From Centers
이 알고리즘은 각 문자와 문자 사이를 중심으로 삼아 좌우로 확장하면서 회문을 찾는 방식. 시간 복잡도는 O(n^2)로, 문자열의 각 문자마다 최대 n번의 확장을 시도하기 때문.
```py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            left = i
            right = j

            # 주어진 중심에서 좌우로 확장하면서 회문인지 검사
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1  # 왼쪽으로 확장
                right += 1  # 오른쪽으로 확장

            # 확장이 멈춘 후 회문의 길이를 반환
            return right - left - 1

        ans = [0, 0]  # 가장 긴 회문의 시작과 끝 인덱스 초기화

        # 문자열의 각 문자 또는 두 문자 사이를 중심으로 회문을 찾음
        for i in range(len(s)):
            # 홀수 길이의 회문 검사 (중심이 하나인 경우)
            odd_length = expand(i, i)
            if odd_length > ans[1] - ans[0] + 1:  # 더 긴 회문을 찾으면
                dist = odd_length // 2
                ans = [i - dist, i + dist]  # 회문의 시작과 끝 인덱스 업데이트

            # 짝수 길이의 회문 검사 (중심이 두 개인 경우)
            even_length = expand(i, i + 1)
            if even_length > ans[1] - ans[0] + 1:  # 더 긴 회문을 찾으면
                dist = (even_length // 2) - 1
                ans = [i - dist, i + 1 + dist]  # 회문의 시작과 끝 인덱스 업데이트

        i, j = ans  # 가장 긴 회문의 시작과 끝 인덱스
        return s[i : j + 1]  # 가장 긴 회문 부분 문자열 반환

```

### Approach 4: Manacher's Algorithm
Palindrome을 linear time 으로 해결하는 방법임
```py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 문자열의 각 문자 사이에 '#'을 추가하고, 시작과 끝에도 '#'을 추가
        s_prime = "#" + "#".join(s) + "#"
        n = len(s_prime)  # 변환된 문자열의 길이
        palindrome_radii = [0] * n  # 각 위치에서 회문의 반지름을 저장하는 배열
        center = radius = 0  # 현재 가장 긴 회문의 중심과 반지름 초기화

        for i in range(n):
            mirror = 2 * center - i  # 현재 문자 i의 거울 인덱스

            # 현재 인덱스 i가 현재 반지름(radius) 내에 있을 경우
            if i < radius:
                palindrome_radii[i] = min(radius - i, palindrome_radii[mirror])

            # i를 중심으로 회문을 확장
            while (
                i + 1 + palindrome_radii[i] < n
                and i - 1 - palindrome_radii[i] >= 0
                and s_prime[i + 1 + palindrome_radii[i]] == s_prime[i - 1 - palindrome_radii[i]]
            ):
                palindrome_radii[i] += 1  # 회문 반지름 증가

            # 회문이 현재 반지름보다 길어지면 중심과 반지름 업데이트
            if i + palindrome_radii[i] > radius:
                center = i
                radius = i + palindrome_radii[i]

        # 가장 긴 회문의 길이와 중심 인덱스 찾기
        max_length = max(palindrome_radii)
        center_index = palindrome_radii.index(max_length)

        # 원래 문자열에서 회문 시작 인덱스 계산
        start_index = (center_index - max_length) // 2
        longest_palindrome = s[start_index : start_index + max_length]  # 가장 긴 회문 부분 문자열 추출

        return longest_palindrome  # 결과 반환

```
