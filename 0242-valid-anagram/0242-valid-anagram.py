from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = defaultdict(int)
        for idx in range(len(s)):
            dic[s[idx]] += 1
            dic[t[idx]] -= 1
        
        for d in dic:
            if dic[d] != 0:
                return False
        return True