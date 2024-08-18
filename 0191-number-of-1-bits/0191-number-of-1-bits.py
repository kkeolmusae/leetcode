class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)
        return b.count("1")