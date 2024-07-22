# 다른 풀이
이거 예전에 백준에서 푼 적 있고 코테에서 자주 나오는 유형임.

시간 복잡도: O(nlogn)

```py
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
```

### 다른 풀이
시간 복잡도: O(n logn)

```py
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # 회의가 없는 경우, 회의실이 필요 없습니다.
        if not intervals:
            return 0

        used_rooms = 0

        # 시작 시간과 종료 시간을 각각 분리하고 정렬합니다.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals])
        L = len(intervals)

        # 알고리즘에 사용할 두 개의 포인터: e_ptr(종료 시간 포인터)와 s_ptr(시작 시간 포인터).
        end_pointer = 0
        start_pointer = 0

        # 모든 회의가 처리될 때까지
        while start_pointer < L:
            # 현재 시작하는 회의의 시작 시간이 이전 회의의 종료 시간보다 크거나 같으면
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # 회의실을 하나 비우고 종료 시간 포인터를 증가시킵니다.
                used_rooms -= 1
                end_pointer += 1

            # 회의실이 비었는지 여부에 관계없이 회의실 사용 수를 증가시킵니다.
            # 회의실이 비었으면, 이 증가 작업은 효과가 없습니다. used_rooms는 동일하게 유지됩니다.
            # 회의실이 비지 않았다면, 사용 중인 회의실 수가 증가합니다.
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms

```