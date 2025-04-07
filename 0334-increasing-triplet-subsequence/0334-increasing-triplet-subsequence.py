class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = math.inf
        second = math.inf
        for curr in nums:
            if curr <= first:
                first = curr
            elif curr <= second:
                second = curr
            else:
                return True

        return False