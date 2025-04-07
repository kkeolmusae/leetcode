class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_idx = 0
        w2_idx = 0
        w1_len = len(word1)
        w2_len = len(word2)

        result = ""
        while w1_idx < w1_len and w2_idx < w2_len:
            result += word1[w1_idx]
            result += word2[w2_idx]
            w1_idx += 1
            w2_idx += 1

        if w1_idx < w1_len:
            result += word1[w1_idx:]
        elif w2_idx < w2_len:
            result += word2[w2_idx:]

        return result
