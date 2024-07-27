from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lidx = 0
        ridx = len(numbers) - 1

        while lidx < ridx:
            left = numbers[lidx]
            right = numbers[ridx]
            sums = left + right

            if target == sums:
                return [lidx + 1, ridx + 1]

            if sums > target:
                ridx -= 1
            elif sums < target:
                lidx += 1