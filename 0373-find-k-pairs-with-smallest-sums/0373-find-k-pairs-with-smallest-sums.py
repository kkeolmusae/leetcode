class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:

        m = len(nums1)
        n = len(nums2)
        result = []

        visited = set()

        min_heap = [(nums1[0] + nums2[0], (0, 0))]  # 제일 앞에 있는 값 두개가 최소 값임
        visited.add((0, 0))  # 사용한 인덱스 저장

        while k > 0:
            _, (i, j) = heapq.heappop(min_heap)
            result.append(
                (nums1[i], nums2[j])
            )  # i,j 인덱스에 해당하는 값들을 result 에 추가

            #  i,j 가 가장 작은 조합이라면, 그 다음으로 작은 조합은 (i+1, j) 또는 (i, j+1) 이다.
            if i + 1 < m and (i + 1, j) not in visited:
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))
            k -= 1

        return result
