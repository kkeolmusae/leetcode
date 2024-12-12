# 풀이
- Difficulty:  Medium
- Topic:  Array / String
- Elapsed Time:  15m
- Status:  O
- Memo: 다시 안풀어봐도 될 문제. 일단 random하게 나와야한다는데 순서가 왜 상관있는지 모르겠음. 

## 내 풀이
처음에는 set 하나로 풀었다가 random 에서 틀리는거 보고 이해 안되서 걍 해설봄
```py
class RandomizedSet():
    def __init__(self):
        self.dict = {}
        self.list = []

        
    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.dict:
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.list)
```
