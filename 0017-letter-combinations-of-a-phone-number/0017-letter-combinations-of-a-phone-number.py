class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not len(digits):
            return result

        pad = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def backtracking(curr: List[str], idx: int):
            if len(curr) == len(digits):
                result.append("".join(curr[:]))
                return

            num = digits[idx]

            for c in pad[num]:
                curr.append(c)
                backtracking(curr, idx + 1)
                curr.pop()

        backtracking([], 0)
        return result