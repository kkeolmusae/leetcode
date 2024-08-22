class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = -math.inf

        q = deque()
        prev = 0
        for idx in range(len(nums)):
            q.append(nums[idx])
            prev += nums[idx]

            if len(q) > k:
                prev -= q.popleft()

            if len(q) == k:
                result = max(result, prev / k)
        return result