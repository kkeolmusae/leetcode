from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x[0])  # 시작 시간이 빠른 순서로 정렬

        endTime = intervals[0][1]  # 가장 빨리 시작하는 강의의 끝나는 시간

        for sTime, eTime in intervals[1:]:
            if sTime < endTime:  # 수업 시작시간이 endTime 보다 작으면 강의 못듣는거임
                return False

            endTime = max(endTime, eTime)  # endTime 갱신
        return True


solution = Solution()