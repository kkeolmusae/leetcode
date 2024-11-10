# 풀이
- Neetcode 150, Medium
- DP
- Time: X
- 처음에 테스트 케이스는 다 맞았는데 예외 케이스 통과 못해서 gpt 돌려서 보완함

## 내 풀이
두자리 디코딩 가능한 경우 원래 단순히 +1을 해줬는데 그러면 안되는거였음.
```py
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # 시작부터 0이면 디코딩 불가
        if s[0] == "0":
            return 0

        dp = [0] * n
        dp[0] = 1  # 시작부터 0은 아니니

        for i in range(1, n):
            # 한자리 디코딩 가능한 경우
            if s[i] != "0":
                # 0이 이니면 이전까지의 경우의 수 그대로 사용가능
                dp[i] = dp[i - 1]

            # 두자리 디코딩 가능한 경우
            if 10 <= int(s[i - 1 : i + 1]) <= 26:
                # 전전까지의 경우의 수 + (이전+현재 로 만들어진 두자리수 케이스) 가 가능한 거니깐
                # 전전까지의 경우의 수를 더해줌 
                if i > 1:
                    dp[i] += dp[i - 2]
                else:
                    # 두번째 문자면 전전이 없기때문에 그냥 1더해줌
                    dp[i] += 1
        return dp[n - 1]

```

## 다른 풀이
### Approach 1: Iterative Approach
```py
class Solution:
    def numDecodings(self, s: str) -> int:
        # 부분 문제 결과를 저장할 배열
        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        # 길이가 1인 문자열의 디코딩 방법은 1입니다.
        # 다만, 문자열이 '0'인 경우는 디코딩이 불가능합니다.
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, len(dp)):
            # 한 자리 숫자로 디코딩이 가능한지 확인
            if s[i - 1] != "0":
                dp[i] = dp[i - 1]

            # 두 자리 숫자로 디코딩이 가능한지 확인
            two_digit = int(s[i - 2 : i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]

```

### Approach 2: Recursive Approach with Memoization
```py
class Solution:

    @lru_cache(maxsize=None)
    def recursiveWithMemo(self, index, s) -> int:
        # 문자열 끝에 도달한 경우
        # 디코딩 성공으로 1을 반환
        if index == len(s):
            return 1

        # 현재 위치의 문자가 '0'이면 디코딩 불가능
        if s[index] == "0":
            return 0

        # 마지막 문자에 도달하면 1을 반환
        if index == len(s) - 1:
            return 1

        # 한 자리 수로 디코딩 가능한 경우
        answer = self.recursiveWithMemo(index + 1, s)
        
        # 두 자리 수로 디코딩 가능한 경우
        if int(s[index : index + 2]) <= 26:
            answer += self.recursiveWithMemo(index + 2, s)

        return answer

    def numDecodings(self, s: str) -> int:
        return self.recursiveWithMemo(0, s)

```

### Approach 3: Iterative, Constant Space
```py
class Solution:
    def numDecodings(self, s: str) -> int:
        # 문자열이 '0'으로 시작하면 디코딩 불가
        if s[0] == "0":
            return 0

        # 두 자리 전 값(two_back)과 한 자리 전 값(one_back)을 초기화
        two_back = 1  # 빈 문자열을 디코딩하는 방법은 1가지
        one_back = 1  # 첫 번째 문자 하나만 디코딩하는 방법도 1가지

        for i in range(1, len(s)):
            current = 0  # 현재 위치에서의 디코딩 방법 수 초기화

            # 한 자리 숫자로 디코딩 가능한 경우
            if s[i] != "0":
                current = one_back

            # 두 자리 숫자로 디코딩 가능한 경우
            two_digit = int(s[i - 1 : i + 1])
            if 10 <= two_digit <= 26:
                current += two_back

            # 이전 두 값 업데이트
            two_back = one_back
            one_back = current

        return one_back

```