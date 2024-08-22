class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        initCnt = 0
        for st in s[:k]:
            if st in "aeiou":
                initCnt += 1

        result = initCnt
        for idx in range(k, len(s)):
            if s[idx] in "aeiou":
                initCnt += 1
            if s[idx - k] in "aeiou":
                initCnt -= 1

            result = max(result, initCnt)
        return result