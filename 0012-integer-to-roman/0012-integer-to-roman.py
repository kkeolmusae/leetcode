class Solution:
    def intToRoman(self, num: int) -> str:
        ex_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ex_str = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        idx = 0

        result = ""
        while idx < len(ex_num) and num > 0:
            tmp = num // ex_num[idx]  # 현재 위치의 숫자로 나눠보고
            # 나눠져서 몫이 나오면
            if tmp > 0:
                result += tmp * ex_str[idx]  # tmp 만큼해당 숫자반복
                num -= ex_num[idx] * tmp
            else:
                idx += 1

        return result