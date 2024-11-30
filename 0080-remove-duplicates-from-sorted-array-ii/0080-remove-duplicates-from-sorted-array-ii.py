class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        MAX_NUM = math.inf
        n = len(nums)
        if n < 3:
            return n
        cnt = 0

        num_idx = []

        for i in range(2, n):
            if nums[i] == nums[i - 1] and nums[i] == nums[i - 2]:
                num_idx.append(i)  # 중복되는 수 위치 저장
                cnt += 1

        for idx in num_idx:  # 중복되는 수를 MAX_NUM으로 치환
            nums[idx] = MAX_NUM

        nums.sort()  # 오름차순 정렬

        for idx in range(n):  # MAX_NUM -> "_" 으로 치환
            if nums[idx] == MAX_NUM:
                nums[idx] = "_"

        return n - cnt
