class Solution:
    def numberCount(self, a: int, b: int) -> int:
        cnt = 0
        for i in range(a, b + 1):
            s = str(i)
            n = len(s)
            sets = set(s)
            if n == len(sets):
                cnt +=1 
        return cnt