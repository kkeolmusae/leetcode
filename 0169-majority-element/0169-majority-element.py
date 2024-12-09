class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = defaultdict(int)
        n = len(nums)
        max_appear_time = n / 2

        for num in nums:
            dict[num] += 1
            if dict[num] >= max_appear_time:
                return num