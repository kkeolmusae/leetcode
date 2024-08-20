class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = math.inf
        second_num = math.inf

        for num in nums:
            if num <= first_num:  # first_num 배치하고
                first_num = num
            elif num <= second_num:
                # first_num 보다 크고 second_num보다 작으면 second_num 배치
                second_num = num
            else:
                # first_num이랑 second_num 보다 크면 조건 중족시킨거니깐
                return True

        return False
