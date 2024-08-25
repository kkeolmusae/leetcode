class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = defaultdict(int)
        for num in arr:  # 숫자 다 count 해놓고
            dic[num] += 1

        s = set()
        for k in dic.keys():
            if dic[k] not in s:
                s.add(dic[k])
            else:  # 해당 count가 set 에 있으면 False
                return False
        return True