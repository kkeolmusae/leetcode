class Solution:
    def reverseVowels(self, s: str) -> str:
        strs = ""
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        for st in s:
            if st in vowels:
                strs += st

        i = 0
        strs = "".join(reversed(strs))

        result = ""
        for idx in range(len(s)):
            st = s[idx]
            if st in vowels:
                result += strs[i]
                i += 1
            else:
                result += st
        return result