from typing import Counter, List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        count = Counter(hand)

        q = []
        while count:
            if not q:
                item = min(count.keys())
                q.append(item)
                if count[item] == 1:
                    del count[item]
                else:
                    count[item] = count[item] - 1
            else:
                next_num = q[-1] + 1
                if not count[next_num]:
                    return False
                else:
                    q.append(next_num)
                    if count[next_num] == 1:
                        del count[next_num]
                    else:
                        count[next_num] = count[next_num] - 1

            if len(q) == groupSize:
                print(q)
                q = []

        if q:
            return False
        return True