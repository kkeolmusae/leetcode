class Solution:
    def isHappy(self, n: int) -> bool:
        hashmap = set()  # 같은 숫자 2번 반복하면 UnHappy임

        while True:
            tmp = list(str(n))
            next_n = 0
            for t in tmp:
                next_n += int(t) ** 2

            if next_n in hashmap:
                break
            hashmap.add(next_n)
            n = next_n
        return True if n == 1 else False