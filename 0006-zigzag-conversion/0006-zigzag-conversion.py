class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = defaultdict(list)
        lidx = 0
        go_down = True

        if numRows == 1:
            return s

        for idx in range(len(s)):
            l[lidx].append(s[idx])  # 문자 추가하기
            lidx = lidx + 1 if go_down else lidx - 1

            if lidx >= numRows or lidx < 0:  # 끝에 다달았으면
                lidx = lidx + 2 if not go_down else lidx - 2
                if go_down == True:
                    go_down = False
                else:
                    go_down = True

        result = ""
        for idx in range(numRows):
            result += "".join(l[idx])
        return result
