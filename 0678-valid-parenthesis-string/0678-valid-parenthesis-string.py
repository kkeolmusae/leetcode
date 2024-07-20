class Solution:
    def checkValidString(self, s: str) -> bool:
        parenthesis = []
        stars = []
        for idx, st in enumerate(s):
            if st == "(":
                parenthesis.append(idx)
            elif st == "*":
                stars.append(idx)
            else:
                if len(parenthesis):
                    parenthesis.pop()
                elif len(stars):
                    stars.pop()
                else:
                    return False
        while len(parenthesis) and len(stars):
            # 마지막 "(" 가 마지막 "*" 보다 인덱스가 크면(더 뒤에 있으면) pop 못하는거라 False
            if parenthesis[-1] > stars[-1]:
                return False
            parenthesis.pop()
            stars.pop()

        return not parenthesis  # "(" 가 있으면 False, 없으면 True