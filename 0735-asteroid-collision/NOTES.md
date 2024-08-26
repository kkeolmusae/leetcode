# 풀이
- LeetCode 75, Medium
- Stack
- Time: 5m 49s
- 처음에 쉽다고 생각했다가 두 행성이 충돌하는 경우 다시 재충돌하는 경우에 대해 생각을 못해서 재귀로 바꾸는데 시간이 조금 더 걸렸고, 
- 두 행성이 충돌하는 경우에 있어서 직전 행성은 양수고 새로 들어오는 행성은 음수인 경우에 대해서만 충돌하는데 이걸 생각 못해서 시간이 더 걸림

## 내 풀이
```py
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def collision(q, asteriod):
            if not q or q[-1] < 0:  # q가 비어있거나 기존값이 직전 행성이 음수면 충돌안하니깐 그냥 넣음
                q.append(asteroid)
            else:
                prev_asteriod = q[-1]

                if asteroid + prev_asteriod == 0:  # 두 행성 크기가 같으면
                    q.pop()  # 원래 있던 행성 폭팔하고 새로 들어온 행성 안넣음 (둘다 폭팔)
                elif asteroid * prev_asteriod > 0:  # 두 부호가 같으면 방향이 같은거니깐
                    q.append(asteroid)  # 그대로 추가
                else:  # 두 행성의 크기가 다른데 절대값이 다르면 충돌하는건데
                    # 새로들어온게 크면 충돌하면서 원래꺼 터짐 (새로 들어온게 작으면 폭팔하는거라 q에 안넣고 끝냄)
                    if abs(prev_asteriod) < abs(asteroid):
                        q.pop()  # 원래 있던 행성 폭팔
                        collision(q, asteriod)  # 직전 행성이랑 다시 비교하기

        q = []
        for asteroid in asteroids:
            collision(q, asteroid)
        return q
```

## 다른 풀이
### Approach 1:
나는 재귀로 짰는데 이거는 재귀로 안짬. 그리고 더 간결한듯..
```py
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            flag = True
            while stack and (stack[-1] > 0 and asteroid < 0):
                # 스택의 맨 위에 있는 소행성이 현재 소행성보다 작으면, 스택에서 제거
                # 이후 스택의 다음 소행성과 비교를 계속 진행
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                
                # 스택의 맨 위 소행성과 현재 소행성의 크기가 같으면 둘 다 소멸
                # 스택에서 소행성을 제거하고 현재 소행성을 스택에 추가하지 않음
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()

                # 현재 소행성이 파괴되므로 스택에 추가하지 않음
                flag = False
                break

            if flag:
                stack.append(asteroid)

        return stack

```

### Approach 2:
```py
```

### Approach 3:
```py
```