class Solution:
    def reverseWords(self, s: str) -> str:
        new_strs = []
        for word in list(reversed(s.split(" "))):
            if word != "":
                new_strs.append(word)
        return " ".join(new_strs)