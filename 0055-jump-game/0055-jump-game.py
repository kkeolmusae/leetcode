class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # nums 길이가 1이면 가능
        if len(nums) == 1:
            return True

        # nums의 첫번째값이 0이면 False (nums 길이가 2이상임)
        if nums[0] == 0:
            return False

        last_idx = len(nums) - 1  # 도달해야하는 지점
        curr = 0  # 현재 위치
        can_jump = nums[curr]  # 최대 점프 가능 위치

        while curr <= can_jump:
            can_jump = max(curr + nums[curr], can_jump)  # 최대 점프 가능 위치 갱신
            if can_jump >= last_idx:  # 점프 가능하면 True
                return True
            curr += 1  # 다음 발판으로
        return False  # last_idx에 도달 못한거니깐 False
