class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ["(", "[", "{"]
        close = [")", "]", "}"]
        for st in s:
            if st in open:
                stack.append(st)
            else:
                if len(stack) == 0:
                    return False
                prev = stack.pop()
                if (st == close[0] and prev != open[0]) or (st == close[1] and prev != open[1]) or (st == close[2] and prev != open[2]):
                    return False
        
        if len(stack) != 0:
            return False
        return True