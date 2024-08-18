import heapq


class MedianFinder:

    def __init__(self):
        self.hi = []  # 큰 숫자들을 min heap으로 넣기
        self.lo = []  # 작은 숫자들을 max heap으로 넣기

    def addNum(self, num: int) -> None:
        heapq.heappush(self.hi, num)  # 일단 hi에 넣고

        # hi에서 제일 작은 값을 lo로 옮김
        heapq.heappush(self.lo, -heapq.heappop(self.hi))

        if len(self.hi) < len(self.lo):
            # lo 에서 가장 큰 숫자를 hi로 옮기자
            heapq.heappush(self.hi, -heapq.heappop(self.lo))

    def findMedian(self) -> float:

        if len(self.lo) == len(self.hi):
            return (-self.lo[0] + self.hi[0]) / 2
        return self.hi[0]