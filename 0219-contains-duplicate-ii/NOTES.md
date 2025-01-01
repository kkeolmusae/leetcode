# 풀이
- Difficulty:  Easy
- Topic:  Hashmap
- Elapsed Time:  4m
- Status:  O
- Memo: 쉬운 문제

## 내 풀이
hashmap에 num 이랑 num의 위치(idx)를 저장해뒀다가 쓰는 방법으로 풀었다.
```py
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
```

## 다른 풀이
### Approach 1: Hash Table
```py
def containsNearbyDuplicate(nums, k):
    seen = set()  # 현재 창(window)에서 본 숫자를 저장하는 집합
    for i in range(len(nums)):
        # 현재 숫자가 집합에 있으면 중복이므로 True 반환
        if nums[i] in seen:
            return True
        # 집합에 현재 숫자를 추가
        seen.add(nums[i])
        # 집합의 크기가 k를 초과하면 가장 오래된 숫자를 제거
        if len(seen) > k:
            seen.remove(nums[i - k])
    # 중복이 발견되지 않으면 False 반환
    return False
```