from typing import List
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 변환: 홀수는 1, 짝수는 0
        nums = [num % 2 for num in nums]
        
        prefix_sum = 0 # 누적 합 
        count = defaultdict(int)
        count[0] = 1 # 각 누적 합이 몇 번 등장했는지를 기록
        result = 0
        
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in count: 
                result += count[prefix_sum - k]
            count[prefix_sum] += 1
        
        return result           
        