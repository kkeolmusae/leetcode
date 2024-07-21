import heapq 
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0]) # 시작 시간이 빠른 강의 순으로 정렬
        
        rooms = []
        heapq.heappush(rooms, intervals[0][1]) # 첫번째 강의의 끝나는 시간 넣기
        
        for startTime, endTime in intervals[1:]:
            if rooms[0] <= startTime: # 다음 강의가 현재 가장빨리 끝나는 강의 뒤로 이어질떄
                heapq.heappop(rooms) # 강의 종료
                
            heapq.heappush(rooms, endTime) # 강의 추가
        
        return len(rooms)