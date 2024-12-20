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
