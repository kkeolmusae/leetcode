class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")

        result = []
        for w in words:
            if w != "":
                result.append(w)
        result.reverse()

        return " ".join(result)