class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 1:
            return strs[0]

        same = 0
        for idx in range(min(len(strs[0]), len(strs[1]))):
            if strs[0][same] == strs[1][same]:
                same += 1
            else:
                break

        for idx in range(1, n - 1):
            if strs[idx][:same] != strs[idx + 1][:same]:
                cnt = 0
                for iidx in range(min(len(strs[idx]), len(strs[idx + 1]))):
                    if strs[idx][iidx] == strs[idx + 1][iidx]:
                        cnt += 1
                    else:
                        break
                same = cnt
        return strs[0][:same]