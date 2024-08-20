class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1

        # 0 개수가 2개이상이면 전체 배열이 0임.
        is_zero_exist = False

        for num in nums:
            if num == 0:
                if is_zero_exist:
                    return [0] * len(nums)
                is_zero_exist = True
            else:
                total *= num

        result = []
        for num in nums:
            if num == 0:  # 0이면 total 을 넣고
                result.append(total)
            elif is_zero_exist:  # 0이 아닌데 전체중에 0이 있으면 0을 넣고
                result.append(0)
            else:  # 0이 아예 없는 경우에는 total // num
                result.append(total // num)

        return result
