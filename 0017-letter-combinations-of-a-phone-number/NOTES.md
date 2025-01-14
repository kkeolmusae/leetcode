# 풀이
- Difficulty:  Medium
- Topic:  Backtracking
- Elapsed Time:  15m
- Status:  O (2 times)
- Memo: 지난번에 푼 코드 봤는데 기억이 안난다. 어쨌든 이번에는 백트래킹으로 풀었다. 감이 잡힐랑 말랑한다.

## 내 풀이
```py
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 결과를 저장할 리스트
        result = []
        # 입력 문자열이 비어 있으면 빈 리스트를 반환
        if not len(digits):
            return result

        # 숫자와 문자 매핑 (전화기의 숫자 패드)
        pad = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        # 백트래킹 함수 정의
        def backtracking(curr: List[str], idx: int):
            # 종료 조건: 현재 조합의 길이가 입력 숫자의 길이와 같을 때
            if len(curr) == len(digits):
                result.append("".join(curr[:]))  # 현재 조합을 문자열로 변환하여 결과 리스트에 추가
                return

            # 현재 숫자에 해당하는 문자 리스트 가져오기
            num = digits[idx]

            # 각 문자에 대해 반복적으로 탐색
            for c in pad[num]:
                curr.append(c)  # 현재 문자를 조합에 추가
                backtracking(curr, idx + 1)  # 다음 숫자로 이동
                curr.pop()  # 현재 문자를 제거하여 백트래킹

        # 백트래킹 시작: 빈 조합(curr)과 시작 인덱스(0) 전달
        backtracking([], 0)
        return result

```

## 다른 풀이
### Approach 1: Backtracking
내 코드랑 방법 자체는 거의 비슷하고, 리스트랑 문자 정도의 차이밖에 없다.
```py
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 입력 문자열이 비어 있는 경우, 빈 리스트 반환
        if len(digits) == 0:
            return []

        # 숫자와 문자 매핑 (전화기의 숫자 패드)
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # 백트래킹 함수 정의
        def backtrack(index, path):
            # 종료 조건: 현재 조합의 길이가 입력 숫자의 길이와 같으면
            if len(path) == len(digits):
                combinations.append("".join(path))  # 조합을 문자열로 변환하여 결과 리스트에 추가
                return  # 백트래킹 종료

            # 현재 숫자에 해당하는 문자 리스트 가져오기
            possible_letters = letters[digits[index]]

            # 각 문자에 대해 반복적으로 탐색
            for letter in possible_letters:
                path.append(letter)  # 현재 문자를 경로에 추가
                backtrack(index + 1, path)  # 다음 숫자로 이동
                path.pop()  # 현재 문자를 제거하여 백트래킹

        # 결과를 저장할 리스트
        combinations = []
        # 백트래킹 시작: 빈 경로와 시작 인덱스(0) 전달
        backtrack(0, [])
        return combinations

```