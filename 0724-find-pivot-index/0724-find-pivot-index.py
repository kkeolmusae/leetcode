class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        l_prev = [0] * n
        for i in range(1, len(nums)):  # 왼쪽부터 pivot 계산
            l_prev[i] = l_prev[i - 1] + nums[i - 1]

        r_prev = [0] * n
        for i in range(len(nums) - 2, -1, -1):  # 오른쪽부터 pivot 계산
            r_prev[i] = r_prev[i + 1] + nums[i + 1]

        for idx in range(n):  # 양쪽 비교해서 값이 같으면 idx 리턴
            if l_prev[idx] == r_prev[idx]:
                return idx
        return -1