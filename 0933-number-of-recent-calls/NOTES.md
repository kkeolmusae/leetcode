# 풀이
- LeetCode 75, Easy
- Queue
- Time: 5m 37s
- 지문을 해석하는데 시간이 좀 걸리고 구현 자체는 아주 금방함

## 내 풀이
```py
class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        range = [t - 3000, t]  # 범위 설정

        while self.q and self.q[0] < range[0]:  # q의 첫번째 값이 범위를 벗어나면
            self.q.popleft()  # pop
        return len(self.q)  # return q 사이즈

```

## 다른 풀이
### Approach 1: Iteration over Sliding Window
내 코드랑 아주 흡사함..
```py
class RecentCounter:

    def __init__(self):
        self.slide_window = deque()

    def ping(self, t: int) -> int:
        self.slide_window.append(t)

        while self.slide_window[0] < t - 3000:
            self.slide_window.popleft()

        return len(self.slide_window)
```

### Approach 2:
```py
```

### Approach 3:
```py
```