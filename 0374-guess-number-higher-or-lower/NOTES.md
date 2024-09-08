# 풀이
- LeetCode 75, Easy
- Binary Search
- Time: 5m
- 문제 이해가 더 어려웠음. n이 내가 맞춰야하는 숫자고, pick이 내가 고른 숫자라고 했을때, 
- guess 라는 api를 써서 guess 의 결과가 1이면 n > pick 인거고, 0이면 맞춘거고, -1 이면 pick < n 인거니깐 pick을 맞춰봐라. 라는 문제임

## 내 풀이
```py
class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = low + (high - low) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g < 0:  # 음수라면 내가 큰 숫자를 고른거니깐 high 낮추기
                high = mid - 1
            else:
                low = mid + 1

        return -1

```

## 다른 풀이
파이썬으로 바꾸기 귀찮아서 이번껀 걍 자바로함
### Approach 1: Brute Force
```java
public class Solution extends GuessGame {
    public int guessNumber(int n) {
        for (int i = 1; i < n; i++)
            if (guess(i) == 0)
                return i;
        return n;
    }
}
```

### Approach 2: Using Binary Search
```java
public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int low = 1;
        int high = n;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int res = guess(mid);
            if (res == 0)
                return mid;
            else if (res < 0)
                high = mid - 1;
            else
                low = mid + 1;
        }
        return -1;
    }
}
```
