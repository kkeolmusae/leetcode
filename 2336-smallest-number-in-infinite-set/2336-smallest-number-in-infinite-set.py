class SmallestInfiniteSet:

    def __init__(self):
        self.is_present = set(list(range(1, 1001)))  # 1~1000까지 set이랑 q에 넣어둠
        self.added_integers = list(range(1, 1001))

    def popSmallest(self) -> int:
        if len(self.added_integers):  # 값이 있으면
            num = heapq.heappop(self.added_integers)
            self.is_present.remove(num)  # pop하고 set에서 삭제
            return num

    def addBack(self, num: int) -> None:
        if not num in self.is_present:  # 값이 없는거면
            self.is_present.add(num)  # set에 넣고
            heapq.heappush(self.added_integers, num)  # q에도 넣고
