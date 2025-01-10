class Solution:
    def check(self, n: int, st: str) -> bool:
        left = 0
        right = 0

        for s in st:
            if s == "(":
                left += 1
            else:
                right += 1

            if right > left or left > n or right > n:
                return False
        return right == n

    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        queue = deque([""])

        while queue:
            curr = queue.popleft()

            if len(curr) == n * 2:
                if self.check(n, curr):
                    answer.append(curr)
                continue
            queue.append(curr + "(")
            queue.append(curr + ")")

        return answer