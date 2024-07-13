from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1  # 목적지 인덱스

        # 제일 뒤에서 한칸 앞에서 부터 0번째까지 반복
        for idx in range(goal - 1, -1, -1):
            # idx 위치에서 최대 nums[idx] 만큼 이동했을떄 goal 이상 갈 수 있으면 도착 가능한거니깐
            if idx + nums[idx] >= goal:
                goal = idx
        if goal == 0:
            return True
        return False