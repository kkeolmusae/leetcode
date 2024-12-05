class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1  # 현재 확인중인 위치
        j = 1  # 중복이 제거된 숫자를 저장할 위치

        while i < len(nums):
            if nums[i] == nums[i - 1]:
                i += 1
                continue
            nums[j] = nums[i]
            i += 1
            j += 1
        return j
