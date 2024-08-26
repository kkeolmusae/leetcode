class Solution:
    def removeStars(self, s: str) -> str:
        q = []

        for st in s:
            if st == "*" and q:
                q.pop()
            else:
                q.append(st)
        return "".join(q)