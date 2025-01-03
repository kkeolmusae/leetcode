class Solution:
    def isValid(self, s: str) -> bool:
        open = ["(", "[", "{"]
        close = [")", "]", "}"]
        if len(s) == 1:
            return False

        q = []
        for st in s:
            if st in open:
                q.append(st)
            else:
                if not q:
                    return False
                op = q.pop()
                if op == open[0] and st != close[0]:
                    return False
                if op == open[1] and st != close[1]:
                    return False
                if op == open[2] and st != close[2]:
                    return False

        return True if not q else False