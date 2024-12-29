class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # nums 길이가 1일때
        if len(nums) == 1:
            return 1 if nums[0] >= target else 0
        lidx = 0
        ridx = 0
        result = math.inf
        total = nums[0]
        sub_array_len = 1

        while ridx < len(nums) and lidx < len(nums):
            if total >= target:
                result = min(sub_array_len, result)
                if lidx <= ridx:
                    total -= nums[lidx]
                    sub_array_len -= 1
                    lidx += 1
                else:
                    ridx += 1
                    total += nums[ridx] if ridx < len(nums) else 0
                    sub_array_len += 1 if ridx < len(nums) else 0
            elif total < target:
                ridx += 1
                total += nums[ridx] if ridx < len(nums) else 0
                sub_array_len += 1 if ridx < len(nums) else 0

        return result if result != math.inf else 0