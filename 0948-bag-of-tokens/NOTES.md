### NOTES

나는 정렬하고 deque에 넣어서 점수가 필요한 경우(face up)인 경우에는 왼쪽껄 pop하고 power가 필요한 경우(face down)에는 오른쪽껄 pop 하는 방식으로 구현했는데 deque 안쓰고 그냥 정렬된 배열에서 인덱스만 좌우에서 중간으로 이동하는 방식으로 해결됨

```python
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        low = 0
        high = len(tokens) - 1
        score = 0
        tokens.sort()

        while low <= high:
            # When we have enough power, play lowest token face-up
            if power >= tokens[low]:
                score += 1
                power -= tokens[low]
                low += 1

            # We don't have enough power to play a token face-up
            # If there is at least one token remaining,
            # and we have enough score, play highest token face-down
            elif low < high and score > 0:
                score -= 1
                power += tokens[high]
                high -= 1

            # We don't have enough score, power, or tokens 
            # to play face-up or down and increase our score
            else:
                return score

        return score       
```