class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        range = [t - 3000, t]  # 범위 설정

        while self.q and self.q[0] < range[0]:  # q의 첫번째 값이 범위를 벗어나면
            self.q.popleft()  # pop
        return len(self.q)  # return q 사이즈
