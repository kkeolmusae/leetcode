class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for idx in range(len(nums)):
            num = nums[idx]
            if target - num in hash_map:
                return [hash_map[target - num], idx]
            hash_map[num] = idx
        return []