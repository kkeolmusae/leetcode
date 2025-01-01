class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = defaultdict(int)

        for n in nums:
            dict[n] += 1

        q = []
        for key, val in dict.items():
            # 빈도가 많은게 우선순위가 높게 하기 위해서 - 붙임
            heapq.heappush(q, (-val, key))

        result = []
        while k:
            val, key = heapq.heappop(q)
            result.append(key)
            k -= 1
        return result