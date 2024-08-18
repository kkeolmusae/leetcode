from typing import List


class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)
        return sum(list(map(int, b[2:])))