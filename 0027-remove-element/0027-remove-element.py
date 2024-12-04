class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        n = len(nums)

        for num in nums:
            if val == num:
                cnt += 1

        for _ in range(cnt):
            nums.remove(val)

        return n - cnt