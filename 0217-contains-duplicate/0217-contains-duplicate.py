class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}

        for n in nums:
            if n in dict:
                return True
            dict[n] = False
        return False