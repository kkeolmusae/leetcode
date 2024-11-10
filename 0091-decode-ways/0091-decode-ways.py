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
