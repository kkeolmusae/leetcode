class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        result = []

        # 문자열이 길이 1인 경우
        if len(s) == 1:
            return [[s]]

        def backtracking(curr: List[str], s: str):

            if len(s) == 0:
                result.append(curr)
                return

            for idx in range(1, len(s) + 1):
                if self.isPalindrome(s[:idx]):  # 팰린드롬이면
                    # 팰린드롬인 부분은 curr에 추가하고, 나머지는 다음으로
                    backtracking(curr + [s[:idx]], s[idx:])

        backtracking([], s)
        return result