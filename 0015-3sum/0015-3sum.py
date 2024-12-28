class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        # 가장 작은 숫자가 0 보다 크면 0을 만들 수 없기에 빈 배열 리턴
        if nums[0] > 0:
            return []

        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # 중복된 숫자는 건너뛰기
                continue
            self.twoSum(i, nums, result)

        return result

    def twoSum(
        self, i: int, nums: List[int], result: List[List[int]]
    ) -> List[List[int]]:
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                result.append([nums[i], nums[lo], nums[hi]])
                while lo < hi and nums[lo] == nums[lo + 1]:  # 중복된 숫자는 건너뛰기
                    lo += 1
                while lo < hi and nums[hi] == nums[hi - 1]:  # 중복된 숫자는 건너뛰기
                    hi -= 1
                lo += 1
                hi -= 1