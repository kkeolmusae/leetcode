class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        # 가장 작은 숫자가 0 보다 크면 0을 만들 수 없기에 빈 배열 리턴
        if nums[0] > 0:
            return []

        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1

        if len(dic) == 1 and dic[0] >= 3:
            return [[0, 0, 0]]

        s = set()
        result = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                a, b = nums[i], nums[j]
                c = 0 - (nums[i] + nums[j])

                if c not in dic:
                    continue

                if a == b and b == c and dic[c] < 3:
                    continue

                if a == b and b != c and dic[c] < 2:
                    continue

                if a == c and a != b and dic[a] < 2:
                    continue

                if b == c and a != b and dic[b] < 2:
                    continue

                tmp = sorted([a, b, c])  # 정렬해서 중복 제거

                if tuple(tmp) not in s:
                    result.append(tmp)
                    s.add(tuple(tmp))

        return result