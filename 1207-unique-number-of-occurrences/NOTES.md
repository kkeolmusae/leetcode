# 풀이
- LeetCode 75, Easy
- Hash Map / Set
- Time: 2m
- 이것도 쉬웠음. 

## 내 풀이
arr 돌면서 count 해놓고, set 써서 count가 한번이라도 중복되면 False
```py
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = defaultdict(int)
        for num in arr:  # 숫자 다 count 해놓고
            dic[num] += 1

        s = set()
        for k in dic.keys():
            if dic[k] not in s:
                s.add(dic[k])
            else:  # 해당 count가 set 에 있으면 False
                return False
        return True
```

## 다른 풀이
### Approach 1: Counting Sort
```py
class Solution:
    # 상수 K를 사용하여 요소들을 비음수로 변환
    K = 1000
    
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = [0] * (2 * self.K + 1)
      
        # 요소들의 빈도를 배열에 저장
        for num in arr:
            freq[num + self.K] += 1
        
        # 빈도 배열을 정렬
        freq.sort()
        
        # 인접한 빈도 수가 동일하다면 빈도 수가 고유하지 않음
        for i in range(2 * self.K):
            if freq[i] != 0 and freq[i] == freq[i + 1]:
                return False
        
        # 모든 요소를 순회하면 빈도 수가 고유함을 의미
        return True

```

### Approach 2: HashMap & HashSet
```py
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 요소들의 빈도를 저장하기 위한 딕셔너리
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        # 빈도 수를 저장하기 위한 집합
        freq_set = set(freq.values())
        
        # 집합의 크기가 딕셔너리의 크기와 동일하다면,
        # 빈도 수가 고유하다는 것을 의미
        return len(freq) == len(freq_set)

```