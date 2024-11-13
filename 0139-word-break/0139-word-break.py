class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        queue = deque([0])
        seen = set()

        while queue:
            start = queue.popleft()

            if start == len(s):  # 다 봤으면 return True
                return True

            for end in range(start + 1, len(s) + 1):  # start 다음부터 s 끝까지 
                if end in seen:  # 봤던 부분 생략
                    continue
                word = s[start:end]  # 단어
                if word in words:  # 있는 단어면
                    queue.append(end)  # queue에 넣어서 다음 start 로 하고
                    seen.add(end)  # 방문(?) 처리

        return False