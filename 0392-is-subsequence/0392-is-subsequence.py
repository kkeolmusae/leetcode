class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        sidx = 0
        tidx = 0

        while tidx < len(t):
            if s[sidx] != t[tidx]:
                tidx += 1
                continue
            sidx += 1
            tidx += 1

            if sidx >= len(s):
                return True
        return False