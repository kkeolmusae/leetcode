# 풀이
- LeetCode 75, Medium
- Two Pointers
- Time: 1m 20s
- 쉽게 풀림. 근데 더 효율적으로 해결하는 방법이 있을 것 같은 느낌

## 내 코드
정렬하고, 왼쪽 오른쪽 비교하는 방식으로 품.
```py
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        cnt = 0

        while i < j:
            left = nums[i]
            right = nums[j]
            if left + right == k:
                i += 1
                j -= 1
                cnt += 1
            elif left + right > k:  # 두 수의 합이 k 보다 크면 큰 수를 작게
                j -= 1
            else:  # 두 수의 합이 k 보다 작으면 작은수를 크게
                i += 1
        return cnt
```

## 다른 풀이
### Approach 1: Brute Force
for 문 두번 돌려서 찾아내는 방법. 비효율적인듯
```py
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for first in range(len(nums)):
            # first가 가리키는 요소가 이미 사용된 경우 건너뜀
            if nums[first] == 0:
                continue
            for second in range(first + 1, len(nums)):
                # second가 가리키는 요소가 이미 사용된 경우 건너뜀
                if nums[second] == 0:
                    continue
                if nums[first] + nums[second] == k:
                    nums[first] = nums[second] = 0
                    count += 1
                    break
        return count
```

### Approach 2: Using Hashmap - Two Pass
hash(dict) 사용해서 푼 문제. 처음에 이렇게 풀려다가 일부러 Two Pointer로 품
```py
from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        map = defaultdict(int)
        count = 0
        
        # 배열의 각 요소의 빈도를 기록
        for num in nums:
            map[num] += 1
        
        for num in nums:
            current = num
            complement = k - num
            if map.get(current, 0) > 0 and map.get(complement, 0) > 0:
                # current와 complement가 같은 경우, 2번 이상 등장해야 쌍을 이룰 수 있음
                if current == complement and map[current] < 2:
                    continue
                # 두 숫자의 빈도를 각각 감소시키고 쌍의 개수를 증가
                map[current] -= 1
                map[complement] -= 1
                count += 1
        
        return count

```

### Approach 3: Using Hashmap - Single Pass
위에 Two Pass 를 효율적으로 바꾼 방법
```py
from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        map = defaultdict(int)
        count = 0
        
        for num in nums:
            current = num
            complement = k - current
            
            # complement가 해시맵에 존재하고 빈도가 0보다 큰지 확인
            if map.get(complement, 0) > 0:
                # complement의 빈도를 1 감소시키고 쌍을 이룬 수 증가
                map[complement] -= 1
                count += 1
            else:
                # 현재 숫자를 해시맵에 추가하거나 빈도를 증가
                map[current] += 1
        
        return count
```


### Approach 4: Two Pointer Approach Using Sort
내 코드랑 비슷함. java로 되어있는데 귀찮아서 걍 그대로 옮김.
```java
class Solution {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);
        int count = 0;
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            if (nums[left] + nums[right] < k) {
                left++;
            } else if (nums[left] + nums[right] > k) {
                right--;
            } else {
                left++;
                right--;
                count++;
            }
        }
        return count;
    }
}
```