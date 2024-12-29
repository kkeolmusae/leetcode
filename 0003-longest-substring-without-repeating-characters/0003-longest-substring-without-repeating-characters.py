class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        idx = {}
        st = ""
        result = 0
        start = 0

        for i in range(len(s)):  # 인덱스 기준으로 탐색
            curr_char = s[i]  # 현재 문자
            # 이미 등장한 문자이고, start 보다 뒤에 있을 때
            if curr_char in idx and idx[curr_char] >= start:
                # idx[curr_char]: 현재 문자의 이전 인덱스
                st = s[idx[curr_char] + 1 : i]  # start ~ 현재 문자까지 슬라이싱
                start = idx[s[i]] + 1  # start 갱신
            st += s[i]  # st 에 현재 문자 추가
            idx[s[i]] = i  # 현재 문자의 인덱스 저장
            result = max(result, len(st))  # 최대 길이 갱신

        return result