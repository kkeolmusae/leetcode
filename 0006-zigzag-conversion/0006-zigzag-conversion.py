class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = defaultdict(str)
        lidx = 0
        go_down = True

        if numRows == 1:
            return s

        for idx in range(len(s)):
            l[lidx] += s[idx]  # 문자 넣기
            lidx = lidx + 1 if go_down else lidx - 1

            if lidx >= numRows or lidx < 0:  # 끝을 넘어갔으면
                lidx = lidx + 2 if not go_down else lidx - 2  # 2칸 +- 해서 직전배열로 이동
                go_down = False if go_down else True  # 방향 전환

        result = ""
        for idx in range(numRows):  # 문자 합치기
            result += l[idx]
        return result