​# 풀이
- Difficulty:  Medium
- Topic:  Array & Hashing
- Elapsed Time:  9m
- Status:  O (2 times)
- Memo: 처음에 풀때는 그냥 정렬한 다음에 숫자가 연속되면 count += 1 하고, 숫자가 끊기는 경우에 result 를 갱신하고 count 를 1에서 시작하게 작업했다. 두번째 풀때는 O(n) 으로 풀기 위해서 고민을 꽤나 했다.

## 내 풀이
주석 그대로 set을 이용했다. set 에 있는거 하나씩 꺼내서 시작숫자가 될 수 있는 거면(현재숫자-1 한 숫자가 없는 경우)그 다음 숫자부터 set을 이용하여 숫자 연속을 체크하였다.
```py
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)  # 모든 숫자 set에 넣어두고
        result = 0

        for num in nums_set:  # 하나씩 꺼냄
            # 꺼낸 숫자보다 작은 숫자가 없으면 (이 숫자가 시작숫자라는 뜻)
            if num - 1 not in nums_set:

                tmp = 1  # 초기값
                curr_num = num  # 시작값
                while curr_num + 1 in nums_set:  # 다음 숫자가 있는지 체크해서 있으면
                    tmp += 1  # tmp += 1
                    curr_num += 1  # 다음 값으로 넘어감

                # 연속 숫자가 끊길때까지 하고 result 갱신
                result = max(tmp, result)
        return result

```

## 다른 풀이
### Approach 1: Brute Force
O(n^3) 으로 정렬로 푸는 것 보다 훨씬 별로다.
```py
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak
```

### Approach 2: Sorting
내가 처음에 풀었던 정렬해서 푸는 방식이다.
```py
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)
```

### Approach 3: HashSet and Intelligent Sequence Building
내 코드와 유사하게 set을 썻다.
```py
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
```