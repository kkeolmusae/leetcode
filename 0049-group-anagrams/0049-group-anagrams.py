class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp = []
        for idx in range(len(strs)):  # 정렬한 문자 추가
            tmp.append("".join(sorted(strs[idx])))

        anagrams = defaultdict(list)
        for idx in range(len(tmp)):  # 정렬한 문자를 key로 하여 그룹화
            anagrams[tmp[idx]].append(strs[idx])

        result = []
        for key in anagrams:  # 그룹화된 문자들을 리스트로 변환
            result.append(anagrams[key])
        return result