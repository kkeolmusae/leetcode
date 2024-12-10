class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1 or nums[0] == 0:
            return 0

        curr = 0  # 현재 위치
        can_jump = 0  # 현재 위치에서 점프 가능한 최대 위치
        can_jump_max = 0  # 최대 점프 가능한 위치
        last_idx = len(nums) - 1  # 마지막 위치
        answer = 0

        while curr < last_idx:
            # 최대 점프 가능한 위치는 지속적으로 갱신
            can_jump_max = max(curr + nums[curr], can_jump_max)

            # 현재 위치에서 점프 가능한 최대 위치에 도달하면
            if curr == can_jump:
                answer += 1  # 점프 횟수 증가
                can_jump = can_jump_max  # 현재 위치에서 점프 가능한 최대 위치 갱신
            curr += 1  # 다음 발판으로
        return answer
