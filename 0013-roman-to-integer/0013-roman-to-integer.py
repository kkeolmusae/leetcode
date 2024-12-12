class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = dic[s[0]]
        for idx in range(1, len(s)):
            total += dic[s[idx]]
            if dic[s[idx - 1]] < dic[s[idx]]:
                total -= (dic[s[idx - 1]]) * 2
        return total