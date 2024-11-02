class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_num = nums[0]
        max_num = nums[0]

        result = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            t_min_num = min(num, min_num * num, max_num * num)
            t_max_num = max(num, max_num * num, min_num * num)
            min_num = t_min_num
            max_num = t_max_num
            result = max(max_num, result)
        return result