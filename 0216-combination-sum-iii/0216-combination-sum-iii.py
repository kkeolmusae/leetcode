class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > n:
            return []

        l = list(combinations(list(range(1, 10)), k))

        result = []
        for nums in l:
            if sum(nums) == n:
                result.append(list(nums))
        return result