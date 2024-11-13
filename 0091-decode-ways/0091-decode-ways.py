class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # 시작부터 0이면 디코딩 불가
        if s[0] == "0":
            return 0

        dp = [0] * n
        dp[0] = 1  # 시작부터 0이 아니니 1개 만들 수 있음

        for i in range(1, n):
            if s[i] != "0":  # 0이 아니면 이전꺼 일단 그대로 받고,
                dp[i] = dp[i - 1]

            if 10 <= int(s[i - 1 : i + 1]) <= 26:  # 합칠 수 있는 숫자면
                if i == 1:
                    # 두번쨰 숫자는 전전값이 없으니깐 걍 1더함
                    dp[i] += 1
                else:
                    # 아니면 전전값 더함. 
                    dp[i] += dp[i - 2]

        return dp[n - 1]