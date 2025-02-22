class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            # i번째 원소 nums[i] 이전의 모든 원소 nums[j](j < i)를 확인
            for j in range(i):
                # nums[i] > nums[j] 이면 nums[i]를 nums[j] 뒤에 붙일 수 있음
                # 즉, dp[j] + 1을 고려하여 dp[i]를 갱신
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)