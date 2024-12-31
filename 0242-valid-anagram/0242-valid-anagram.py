class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter_s = Counter(s)
        counter_t = Counter(t)

        for char, count in counter_s.items():
            if counter_t[char] != count:
                return False
        return True