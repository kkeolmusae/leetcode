class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = "".join(sorted(s1))
        window_size = len(s1)
        lidx = 0

        while lidx + window_size <= len(s2):
            tmp = "".join(sorted(s2[lidx : lidx + window_size]))
            if s1 == tmp:
                return True
            lidx += 1
        return False