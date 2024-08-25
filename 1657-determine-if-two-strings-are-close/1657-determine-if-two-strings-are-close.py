class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for w in list(word1):
            d1[w] += 1

        for w in list(word2):
            if w not in d1:  # 문자가 존재하지 않으면 걍 return False
                return False
            d2[w] += 1

        if sorted(d1.values()) == sorted(d2.values()):  # 정렬한 두 배열이 같으면 
            return True
        return False