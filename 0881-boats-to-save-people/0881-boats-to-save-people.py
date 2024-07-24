from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        lidx = 0
        ridx = len(people) - 1

        answer = 0
        while lidx <= ridx:
            left = people[lidx]
            right = people[ridx]
            if left + right <= limit:
                lidx += 1
                ridx -= 1
                answer += 1
            else:
                ridx -= 1
                answer += 1
        return answer