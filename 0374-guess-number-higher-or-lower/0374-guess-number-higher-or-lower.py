# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = low + (high - low) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g < 0:  # 음수라면 내가 큰 숫자를 고른거니깐 high 낮추기
                high = mid - 1
            else:
                low = mid + 1

        return -1
