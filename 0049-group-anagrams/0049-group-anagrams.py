from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        
        for str in strs:
            sorted_str = sorted(str)
            dic["".join(sorted_str)].append(str)
        return list(dic.values())