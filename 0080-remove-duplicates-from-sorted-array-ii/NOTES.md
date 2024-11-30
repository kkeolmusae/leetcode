# 풀이
- Medium
- Array / String
- Time: 10m 
- 문제 주의사항? 에서 extra space 를 사용하지 말라고 해서 약간 고민을 더 했다. 

## 내 풀이
nums 길이가 3 * 10^4 밖에 안되는 것을 보고 O(n^2)만 아니면 괜찮을 것 같아서 다음과 같이 풀었다.
```py
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        MAX_NUM = math.inf

        n = len(nums)
        if n < 3:
            return n
        cnt = 0

        num_idx = []

        for i in range(2, n):
            if nums[i] == nums[i - 1] and nums[i] == nums[i - 2]:
                num_idx.append(i)  # 중복되는 수 위치 저장
                cnt += 1

        for idx in num_idx:  # 중복되는 수를 MAX_NUM으로 치환
            nums[idx] = MAX_NUM

        nums.sort()  # 오름차순 정렬

        for idx in range(n):  # MAX_NUM -> "_" 으로 치환
            if nums[idx] == MAX_NUM:
                nums[idx] = "_"

        return n - cnt

```

## 다른 풀이
### Approach 1: Popping Unwanted Duplicates
리스트 nums에서 최대 두 번까지의 중복을 허용하며 중복된 요소를 제거하는 방법. pop을 사용해서 새로운 배열을 할당하지 않고 구현했다.
```py
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 리스트가 비어있는 경우 예외 처리
        if not nums:
            return 0

        # 리스트의 현재 위치를 가리키는 포인터
        i = 1
        # 현재 숫자의 등장 횟수
        count = 1

        # 리스트의 두 번째 요소부터 순회
        while i < len(nums):
            # 현재 숫자가 이전 숫자와 같은지 확인
            if nums[i] == nums[i - 1]:
                # 현재 숫자의 등장 횟수 증가
                count += 1
                # 등장 횟수가 2회를 초과하면 현재 요소 제거
                if count > 2:
                    nums.pop(i)
                    i -= 1
                    count -= 1
            else:
                # 새로운 숫자가 나타나면 등장 횟수 초기화
                count = 1
            # 다음 요소로 이동
            i += 1

        # 리스트의 새로운 길이 반환
        return len(nums)

```

### Approach 2: Overwriting unwanted duplicates
- 배열을 순회하면서 만약 2번이상 나온 숫자면 해당 숫자를 다음에 나오는 숫자로 overwrite 하고 마지막에 overwrite 한 숫자만큼 뒤에서 삭제함. 
- overwrite 를 하다보면 결국 2번이상 나온 숫자의 개수만큼 배열에서 가장 큰 숫자가 뒤쪽에 위치하게 됨
```py
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 리스트가 비어있는 경우 처리
        if not nums:
            return 0

        # i: 입력 리스트를 순회하는 포인터로, 현재 확인 중인 요소를 가리킴
        # j: 중복이 제거된 숫자를 저장할 위치를 가리키는 포인터
        i = 1
        j = 1
        # 현재 숫자의 등장 횟수
        count = 1

        # 리스트를 순회하며 중복을 제거
        while i < len(nums):
            # 현재 숫자가 이전 숫자와 같은 경우
            if nums[i] == nums[i - 1]:
                count += 1
                # 등장 횟수가 2회를 초과하면 건너뛰기
                if count > 2:
                    i += 1
                    continue
            else:
                # 새로운 숫자가 나타나면 등장 횟수 초기화
                count = 1
            # 중복 허용 범위 내의 숫자를 저장
            nums[j] = nums[i]
            j += 1
            i += 1

        # 리스트의 나머지 부분 삭제
        del nums[j:]
        # 중복 제거 후의 리스트 길이 반환
        return len(nums)

```