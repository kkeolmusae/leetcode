class Solution:
    def getArray(self, digits: str, i: int, res: list, digitToChars: list) -> list:
        # 끝난 경우 (자릿수 오버되는 경우)
        if len(digits) <= i:
            return res

        digit = int(digits[i])
        res2 = []

        if not len(res):  # 최초
            for char in digitToChars[digit]:
                res2.append(char)
        else:  # 이전 결과에 새로운 문자 조합해서 새 결과 리스트 생성
            for elem in res:
                for char in digitToChars[digit]:
                    res2.append(elem + char)

        # 다음 자리로 재귀 호출
        return self.getArray(digits, i + 1, res2, digitToChars)

    def letterCombinations(self, digits: str) -> list:
        if not digits:
            return []

        # 숫자와 문자 매핑 테이블
        digitToChars = [
            [],
            [],
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"],
            ["j", "k", "l"],
            ["m", "n", "o"],
            ["p", "q", "r", "s"],
            ["t", "u", "v"],
            ["w", "x", "y", "z"],
        ]

        res = []
        return self.getArray(digits, 0, res, digitToChars)