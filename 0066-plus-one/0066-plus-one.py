class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(str(n) for n in digits))
        num2 = num + 1
        return [int(n) for n in str(num2)]