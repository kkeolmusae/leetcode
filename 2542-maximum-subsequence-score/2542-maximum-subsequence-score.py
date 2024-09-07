class Solution:

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # nums1[i] 랑 nums2[i] 의 pair로 묶음
        pairs = [(a, b) for a, b in zip(nums1, nums2)]

        # nums2의 값으로 내림차순 정렬.
        # 왜냐하면 nums2에서 k개의 값중 최소값을 곱해야하는데 "num2의 k개 묶음"의 최솟값이 최대값이되는걸 찾기 위함
        pairs.sort(key=lambda x: -x[1])

        k_nums1 = [x[0] for x in pairs[:k]]  # k개 num1
        k_sum_nums1 = sum(k_nums1)  # k개 num1의 합
        heapq.heapify(k_nums1)  # heapq로 변환

        # 일단 pairs[0] ~ pairs[k] 에 대한 결과를 초기값으로 해두고 뒤에 k+1 ~ 갱신
        result = k_sum_nums1 * pairs[k - 1][1]

        # k+1 부터
        for idx in range(k, len(nums1)):
            k_sum_nums1 += pairs[idx][0]  # 일단 값 더해주고
            k_sum_nums1 -= heapq.heappop(k_nums1)  # num1 중에 낮은거 빼주고
            heapq.heappush(k_nums1, pairs[idx][0])  # k_nums1 갱신

            # 최대값 갱신. pairs는 num2 기준 내림차순이라 [idx][1] 이 최소값
            result = max(result, k_sum_nums1 * pairs[idx][1])

        return result