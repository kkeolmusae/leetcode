class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        # 모든 숫자의 합이 홀수면 같은 subset 이 두개 안나옴
        if total_sum % 2 != 0:
            return False

        # subset_sum = 만들고자 하는 숫자 (부분수열의 합)
        subset_sum = total_sum // 2
        n = len(nums)

        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            curr = nums[i - 1]  # 현재 숫자
            for j in range(subset_sum + 1):
                if curr > j:  # 현재 숫자 > 만들고자 하는 숫자
                    # 현재 숫자 빼고 이전 숫자들로 j 만들수 있는지
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 현재 숫자 빼고 이전 숫자들로 j 만들 수 있는지,
                    # 또는 이전 숫자들로 (만들고자 하는 수 - 현재 숫자)를 만들 수 있는지
                    # (= 현재 숫자 포함하면 만들고자 하는 수 만들 수 있는지)
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]

        return dp[n][subset_sum]