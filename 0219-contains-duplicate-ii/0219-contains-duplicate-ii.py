class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for idx in range(len(nums)):
            num = nums[idx]
            if num not in hashmap:
                hashmap[num] = idx
            else:
                dist = abs(idx - hashmap[num])  # 거리
                if dist <= k:
                    return True
                else:
                    hashmap[num] = idx
        return False