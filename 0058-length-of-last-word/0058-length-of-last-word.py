class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        for lidx in range(len(s) - 1, -1, -1):
            if s[lidx] != " ":
                cnt += 1
            elif cnt > 0 and s[lidx] == " ":
                return cnt
        return cnt