class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s2t = {}  # s를 t로 바꾸는 매핑
        t2s = {}  # t를 s로 바꾸는 매핑

        for i in range(len(s)):
            # s를 t로 바꾸는 매핑이 이미 존재하고, t[i]와 다르다면 => False
            if s[i] in s2t and s2t[s[i]] != t[i]:
                return False
            # t를 s로 바꾸는 매핑이 이미 존재하고, t[i]와 다르다면 => False
            if t[i] in t2s and t2s[t[i]] != s[i]:
                return False

            s2t[s[i]] = t[i]  # s[i]를 t[i]로 바꾸는 매핑
            t2s[t[i]] = s[i]  # t[i]를 s[i]로 바꾸는 매핑
        return True