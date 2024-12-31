class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split_s = s.split()
        if len(pattern) != len(split_s):
            return False

        pattern_dict = {}
        word_dict = {}

        for p, w in zip(pattern, split_s):  # 하나씩 꺼내서
            if p not in pattern_dict:  # 없으면 추가
                pattern_dict[p] = w
            else:
                if pattern_dict[p] != w:  # 있으면 dict에 있는 값과 비교
                    return False

            if w not in word_dict:
                word_dict[w] = p
            else:
                if word_dict[w] != p:
                    return False

        return True