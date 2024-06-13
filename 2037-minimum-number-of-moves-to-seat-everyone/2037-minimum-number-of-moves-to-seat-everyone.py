from typing import List
import heapq


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = len(seats)
        heapq.heapify(seats)
        heapq.heapify(students)
        
        count = 0
        for _ in range(n):
            seat = heapq.heappop(seats)
            student = heapq.heappop(students)
            
            count += abs(seat - student)

        return count