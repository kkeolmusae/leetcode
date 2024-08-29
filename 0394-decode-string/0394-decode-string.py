class Solution:
    def decodeString(self, s: str) -> str:
        q = []

        for st in s:
            if st == "]":  # 닫는 문자일때
                temp = ""
                while q and q[-1] != "[":  # 열린 문자가 나올때까지
                    temp = q.pop() + temp

                q.pop()  # 열린 문자삭제

                nums = ""

                while q and q[-1].isdigit():  # 숫자처리. 숫자가 한글자가 아닐 수 있음
                    nums = q.pop() + nums

                q.append(int(nums) * temp)
            else:
                q.append(st)

        return "".join(q)