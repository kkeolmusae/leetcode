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

        for length in range(n, 0, -1):  # n길이부터 0까지 감소
            for idx in range(n - length + 1):
                # 발견하면 그게 긴거임
                if self.checkPalindrome(s, idx, idx + length - 1):
                    return s[idx : idx + length]