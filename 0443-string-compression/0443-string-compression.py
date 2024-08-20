class Solution:
    def compress(self, chars: List[str]) -> int:
        prev_ch = ""
        cnt = 0

        result = ""
        for c in chars:
            if c != prev_ch:
                result += prev_ch
                if cnt > 1:
                    result += str(cnt)
                prev_ch = c
                cnt = 1
            else:
                cnt += 1

        result += prev_ch
        if cnt > 1:
            result += str(cnt)

        for idx in range(len(result)):
            chars[idx] = result[idx]

        return len(result)
