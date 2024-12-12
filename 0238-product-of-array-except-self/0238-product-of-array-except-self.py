class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        product_except_zero = 1
        n = len(nums)

        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                product_except_zero *= num

        result = [0] * n
        # 0 이 2개 이상있는 경우
        if zero_cnt > 1:
            return result

        if zero_cnt == 1:
            for idx in range(n):
                num = nums[idx]
                if num == 0:
                    result[idx] = product_except_zero
        else:
            for idx in range(n):
                num = nums[idx]
                result[idx] = product_except_zero // num
        return result