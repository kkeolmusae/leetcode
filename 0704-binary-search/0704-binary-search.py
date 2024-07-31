from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0  # 맨 처음 위치
        end = len(nums) - 1  # 맨 마지막 위치

        while start <= end:
            mid = (start + end) // 2  # 중간값

            if nums[mid] == target:
                return mid  # target 위치 반환

            elif nums[mid] > target:  # target이 작으면 왼쪽을 더 탐색
                end = mid - 1
            else:  # target이 크면 오른쪽을 더 탐색
                start = mid + 1
        return -1