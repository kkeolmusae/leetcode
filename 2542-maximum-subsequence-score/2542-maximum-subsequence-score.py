class Solution:

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # nums1[i] 랑 nums2[i] 의 pair로 묶음
        pairs = [(a, b) for a, b in zip(nums1, nums2)]

        # nums2의 값으로 내림차순 정렬.
        # 왜냐하면 nums2에서 k개의 값중 최소값을 곱해야하는데 "num2의 k개 묶음"의 최솟값이 최대값이되는걸 찾기 위함
        pairs.sort(key=lambda x: -x[1])

        k_num1 = [x[0] for x in pairs[:k]]  # nums1 k개 꺼내고
        k_num1_sum = sum(k_num1)  # 합 계산
        heapq.heapify(k_num1)  # heapq로 변환(n1 작은거 부터 빼기위함)

        # 일단 pairs[0] ~ pairs[k-1] 에 대한 결과를 초기값으로 해두고 뒤에 k+1 ~ 갱신
        result = k_num1_sum * pairs[k - 1][1]

        # k 부터
        for n1, n2 in pairs[k : len(nums1)]:
            k_num1_sum -= heapq.heappop(k_num1)  # n1중에 작은거 빼고
            k_num1_sum += n1  # 새로 들어온거 추가하고
            heapq.heappush(k_num1, n1)  # k_num1 갱신

            # 최대값 갱신. pairs는 num2 기준 내림차순이라 n2가 최소값
            result = max(result, k_num1_sum * n2)

        return result