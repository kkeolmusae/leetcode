class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0  # write index
        cnt = 1

        for cidx in range(1, len(chars)):
            if chars[cidx] == chars[cidx - 1]:
                cnt += 1
            else:
                chars[i] = chars[cidx - 1]
                i += 1
                if cnt > 1:
                    for c in str(cnt):
                        chars[i] = c
                        i += 1
                cnt = 1

        # 마지막 문자 처리
        chars[i] = chars[-1]
        i += 1
        if cnt > 1:
            for c in str(cnt):
                chars[i] = c
                i += 1

        return i