# 풀이
- Difficulty:  Medium
- Topic:  Array / String
- Elapsed Time:  5m
- Status:  O (3 times)
- Memo: 어쩌다 보니 3번째 풀게됨. 좀 더 쉽게 코드를 짬

## 내 풀이
```py
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        product_except_zero = 1
        n = len(nums)

        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                product_except_zero *= num

        result = [0] * n
        # 0 이 2개 이상있는 경우
        if zero_cnt > 1:
            return result

        if zero_cnt == 1:
            for idx in range(n):
                num = nums[idx]
                if num == 0:
                    result[idx] = product_except_zero
        else:
            for idx in range(n):
                num = nums[idx]
                result[idx] = product_except_zero // num
        return result

```

## 다른 풀이

### Approach 1: Left and Right product lists
왼쪽/오른쪽으로 나눠서 계산을하고, 마지막에 두개를 곱해서 배열을 구함. 

```py
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # 입력 배열의 길이
        length = len(nums)

        # L, R, answer 배열을 정의합니다.
        # L은 각 인덱스의 왼쪽에 있는 모든 원소의 곱을 저장
        # R은 각 인덱스의 오른쪽에 있는 모든 원소의 곱을 저장
        # answer는 최종 결과를 저장
        L, R, answer = [0] * length, [0] * length, [0] * length

        # L[i]는 i번째 인덱스의 왼쪽에 있는 모든 원소들의 곱을 저장
        # 참고: 인덱스 '0'의 경우 왼쪽에 원소가 없으므로 L[0]은 1이 됩니다.
        L[0] = 1
        for i in range(1, length):
            # L[i - 1]은 이미 인덱스 'i - 1'의 왼쪽에 있는 원소들의 곱을 가지고 있습니다.
            # 이를 nums[i - 1]과 곱하면 인덱스 'i'의 왼쪽에 있는 모든 원소들의 곱을 얻을 수 있습니다.
            L[i] = nums[i - 1] * L[i - 1]

        # R[i]는 i번째 인덱스의 오른쪽에 있는 모든 원소들의 곱을 저장
        # 참고: 인덱스 'length - 1'의 경우 오른쪽에 원소가 없으므로 R[length - 1]은 1이 됩니다.
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            # R[i + 1]은 이미 인덱스 'i + 1'의 오른쪽에 있는 원소들의 곱을 가지고 있습니다.
            # 이를 nums[i + 1]과 곱하면 인덱스 'i'의 오른쪽에 있는 모든 원소들의 곱을 얻을 수 있습니다.
            R[i] = nums[i + 1] * R[i + 1]

        # 최종 결과 배열을 만듭니다.
        for i in range(length):
            # 첫 번째 원소의 경우, R[i]가 자기 자신을 제외한 곱이 됩니다.
            # 배열의 마지막 원소의 경우, L[i]가 자기 자신을 제외한 곱이 됩니다.
            # 그 외의 경우, 왼쪽의 곱과 오른쪽의 곱을 곱한 값을 answer에 저장합니다.
            answer[i] = L[i] * R[i]

        return answer
```

#### 공간 복잡도가 O(1) 인 방법
좀 기가 막히게 풀었음. 
왼쪽과 오른쪽의 곱을 각각 계산한 후 이를 결합하여 최종 결과를 얻는 방식으로, 추가 배열을 사용하지 않고 O(n)의 시간 복잡도와 O(1)의 공간 복잡도로 문제를 해결함.
```py
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # 입력 배열의 길이
        length = len(nums)

        # 반환할 결과 배열
        answer = [0] * length

        # answer[i]는 i번째 인덱스의 왼쪽에 있는 모든 원소들의 곱을 저장합니다.
        # 참고: 인덱스 '0'의 경우 왼쪽에 원소가 없으므로 answer[0]은 1로 설정합니다.
        answer[0] = 1
        for i in range(1, length):
            # answer[i - 1]은 이미 인덱스 'i - 1'의 왼쪽에 있는 원소들의 곱을 가지고 있습니다.
            # 이를 nums[i - 1]과 곱하면 인덱스 'i'의 왼쪽에 있는 모든 원소들의 곱을 얻을 수 있습니다.
            answer[i] = nums[i - 1] * answer[i - 1]

        # R은 i번째 인덱스의 오른쪽에 있는 모든 원소들의 곱을 저장합니다.
        # 참고: 인덱스 'length - 1'의 경우 오른쪽에 원소가 없으므로 R은 1로 시작합니다.
        R = 1
        for i in reversed(range(length)):
            # 인덱스 'i'에 대해, R은 오른쪽에 있는 모든 원소들의 곱을 포함하게 됩니다.
            # answer[i]에 현재의 R 값을 곱해줍니다.
            answer[i] = answer[i] * R
            # R을 업데이트하여 다음 인덱스를 위한 오른쪽 곱을 계산합니다.
            R *= nums[i]

        return answer
```