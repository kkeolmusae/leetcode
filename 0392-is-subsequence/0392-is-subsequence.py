class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        n = len(s)
        m = len(t)

        if n > m:
            return False

        while i <= n - 1 and j <= m - 1:
            if s[i] == t[j]:  # 같으면
                i += 1
                j += 1
            else:
                j += 1  # j 만 칸 뒤로 가기

        if i == n:
            return True
        return False