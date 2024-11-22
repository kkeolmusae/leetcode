# 풀이
- Medium
- Stack
- Time: 10m
- 쉬운문제인데 오랜만에 풀어서 시간이 오래 걸렸다.

## 내 풀이
```py
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for st in path.split("/"):
            if st == "": # 빈값이면 패스
                continue
            
            # .. 이면 한칸 위로 가야하니깐 pop
            if st == ".." and len(stack): 
                stack.pop()
            elif st != ".." and st != ".":
                # .. 이나 . 이 아니면 stack에 넣기
                stack.append(st)
        return "/" + "/".join(stack)
```

## 다른 풀이
### Approach: Using Stacks
내 코드랑 얼추 비슷하다.
```py
class Solution:
    def simplifyPath(self, path: str) -> str:

        # 스택을 초기화합니다.
        stack = []

        # 입력 문자열을 "/"로 나누어 각 부분을 처리합니다.
        for portion in path.split("/"):

            # 현재 요소가 ".."인 경우,
            # 스택이 비어 있지 않다면 스택에서 하나를 꺼냅니다.
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                # 요소가 "."이거나 빈 문자열인 경우 아무 작업도 하지 않습니다.
                continue
            else:
                # 유효한 디렉토리 이름인 경우 스택에 추가합니다.
                stack.append(portion)

        # 모든 디렉토리 이름을 "/"로 연결하여 최종 문자열을 만듭니다.
        final_str = "/" + "/".join(stack)
        return final_str

```