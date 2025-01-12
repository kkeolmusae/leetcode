class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        def backtracking(curr: List[int], startIdx: int):
            result.append(curr[:])

            for i in range(startIdx, n):
                if i > startIdx and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                backtracking(curr, i + 1)
                curr.pop()

        backtracking([], 0)
        return result