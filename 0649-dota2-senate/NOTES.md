# 풀이
- LeetCode 75, Medium
- Queue
- Time: 25m 45s
- 일단 문제 자체를 이해하는데 걸린 시간이 좀 길었고, 구현도 효율적인 방법을 찾다가 30분 넘어갈 것 같아서 일단 품
- 다음 상원이 현재 상원이랑 같으면 그 뒤에 다른 상원 하나를 없앨 수 있고
- 다음 상원이 현재 상원이랑 다르면 바로 뒤의 상원을 없앨 수 있음

## 내 풀이
문제 조건 그대로 풀었는데 remove 랑 count 하는 부분에서 시간을 많이 써서 시간복잡성 측면에서 별로임 (O(n<sup>2</sup>))
```py
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(list(senate))

        current_senator = queue[0]
        while queue:
            curr = queue.popleft()
            if queue and queue[0] != curr:  # 현재 상원이 다음 상원이랑 다르면
                queue.popleft()  # 다음 상원 제거
            elif queue:
                other = "R" if curr == "D" else "D"
                if other in queue:  # 뒤에 있는 다른 상원 제거
                    queue.remove(other)
            current_senator = curr  # 현재 상원 업데이트
            queue.append(curr)  # 제일 뒤 라운드로

            if (queue.count("R") or queue.count("D")) == len(queue):
                break
        return "Radiant" if current_senator == "R" else "Dire"
```

## 다른 풀이
### Approach 1: Greedy
이것도 O(n<sup>2</sup>)으로 풀림. 
```py
class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        # 문자열은 변경할 수 없으므로 리스트로 변환하여 가공합니다.
        # 리스트에는 투표에서 제거되지 않은 의원들만 남습니다.
        senate = list(senate)

        # 승리자를 판단하기 위해 'R'과 'D'의 숫자를 셉니다.
        r_count = senate.count('R')
        d_count = len(senate) - r_count

        # 'to_ban'을 'start_at' 위치에서 가장 가까운 다음 후보를 금지합니다.
        # 리스트를 순환해야 한다면, 다음 턴에도 동일한 인덱스의 의원 차례가 됩니다.
        # 순환 여부를 반환합니다.
        def ban(to_ban, start_at):

            loop_around = False
            pointer = start_at

            while True:
                if pointer == 0:
                    loop_around = True
                if senate[pointer] == to_ban:
                    senate.pop(pointer)  # 금지된 의원 제거
                    break
                pointer = (pointer + 1) % len(senate)

            return loop_around

        # 현재 투표할 의원의 인덱스
        turn = 0

        # 승리자가 결정될 때까지 반복합니다.
        while r_count > 0 and d_count > 0:

            # 다음 상대를 금지합니다. 다음 인덱스에서 시작합니다.
            # % 연산으로 리스트의 끝을 넘어가면 처음으로 돌아갑니다.
            if senate[turn] == 'R':
                banned_senator_before = ban('D', (turn + 1) % len(senate))
                d_count -= 1  # 'D' 의원 수 감소
            else:
                banned_senator_before = ban('R', (turn + 1) % len(senate))
                r_count -= 1  # 'R' 의원 수 감소

            # 금지된 의원의 인덱스가 현재 의원의 인덱스보다 앞이라면,
            # 리스트에서 의원이 제거되었으므로 turn을 1 감소시킵니다.
            if banned_senator_before:
                turn -= 1

            # 다음 투표로 넘어갑니다.
            turn = (turn + 1) % len(senate)

        # 남아 있는 의원 수에 따라 승리자를 반환합니다.
        return 'Radiant' if d_count == 0 else 'Dire'

```

### Approach 2: Boolean Array
이것도 O(n<sup>2</sup>). Approach 1이랑 ben 하는 함수가 조금 다름
```py
class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        # 상원의원 수
        N = len(senate)

        # 상원의원이 금지되었는지 표시하는 리스트
        banned = [False] * N

        # 금지되지 않은 각 종류의 상원의원 수
        r_count = senate.count('R')  # Radiant 당 상원의원 수
        d_count = N - r_count         # Dire 당 상원의원 수

        # "to_ban" 유형의 상원의원을 "start_at" 다음 인덱스에서 금지
        def ban(to_ban, start_at):
            # "to_ban" 유형의 다음으로 적합한 상원의원을 찾음
            # 찾으면 그 상원의원을 금지로 표시
            pointer = start_at
            while True:
                if senate[pointer] == to_ban and not banned[pointer]:
                    banned[pointer] = True
                    break
                pointer = (pointer + 1) % len(senate)  # 순환 구조로 인덱스 업데이트

        # 현재 턴의 상원의원 인덱스
        turn = 0

        # 두 당 모두 최소한 한 명의 상원의원이 남아있는 동안 반복
        while r_count > 0 and d_count > 0:

            # 현재 턴의 상원의원이 금지되지 않았다면
            if not banned[turn]:
                if senate[turn] == 'R':
                    ban('D', (turn + 1) % N)  # 다음 Dire 상원의원을 금지
                    d_count -= 1  # Dire 상원의원 수 감소
                else:
                    ban('R', (turn + 1) % N)  # 다음 Radiant 상원의원을 금지
                    r_count -= 1  # Radiant 상원의원 수 감소

            # 턴을 다음 상원의원으로 넘김
            turn = (turn + 1) % N

        # Dire 당 상원의원이 더 이상 없으면 Radiant 승리, 반대의 경우 Dire 승리
        return 'Radiant' if d_count == 0 else 'Dire'

```

### Approach 4: Two Queues 
queue 를 두개 쓰는 방법으로 O(n) 으로 해결됨
```py
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        # 상원의원 수
        n = len(senate)

        # 상원의원의 인덱스를 저장하는 큐
        # 인덱스를 사용해 상원의원의 다음 턴을 결정
        r_queue = deque()  # Radiant 당 상원의원의 인덱스 큐
        d_queue = deque()  # Dire 당 상원의원의 인덱스 큐

        # 큐를 채우기
        for i, s in enumerate(senate):
            if s == 'R':
                r_queue.append(i)  # Radiant 상원의원의 인덱스를 큐에 추가
            else:
                d_queue.append(i)  # Dire 상원의원의 인덱스를 큐에 추가

        # 두 당에 모두 상원의원이 남아 있는 동안 반복
        while r_queue and d_queue:
            
            # 각 당의 다음 턴 상원의원의 인덱스를 큐에서 꺼냄
            r_turn = r_queue.popleft()
            d_turn = d_queue.popleft()

            # 더 작은 인덱스를 가진 상원의원이 큰 인덱스를 가진 상원의원을 금지
            # 작은 인덱스의 상원의원이 다음 라운드에서 다시 턴을 가짐
            if d_turn < r_turn:
                d_queue.append(d_turn + n)  # Dire 상원의원을 다음 라운드에 추가
            else:
                r_queue.append(r_turn + n)  # Radiant 상원의원을 다음 라운드에 추가
        
        # 빈 큐가 된 당이 패배, 남아 있는 당이 승리
        return "Radiant" if r_queue else "Dire"

```

### Approach 5: Single Queue
내가 해결하고 싶었던 방식
```py
class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        # 각 당의 현재 상원의원 수
        r_count = senate.count('R')  # Radiant 당 상원의원 수
        d_count = len(senate) - r_count  # Dire 당 상원의원 수

        # 상대 당의 상원의원을 금지할 수 있는 '부유하는' 금지 횟수
        d_floating_ban = 0  # Dire 당에 대한 금지 횟수
        r_floating_ban = 0  # Radiant 당에 대한 금지 횟수

        # 상원의원들을 저장하는 큐
        q = deque(senate)

        # 어느 한 당의 상원의원이 모두 금지될 때까지 반복
        while r_count and d_count:

            # 현재 차례의 상원의원을 큐에서 꺼냄
            curr = q.popleft()

            # 현재 상원의원이 금지되지 않은 경우, 상대 당을 금지하고 다시 큐에 추가
            # 금지된 경우, 해당 당의 금지 횟수와 상원의원 수를 감소
            if curr == 'D':
                if d_floating_ban:
                    d_floating_ban -= 1  # Dire 당에 대한 금지 횟수 감소
                    d_count -= 1  # Dire 당 상원의원 수 감소
                else:
                    r_floating_ban += 1  # Radiant 당에 대한 금지 횟수 증가
                    q.append('D')  # Dire 상원의원을 다시 큐에 추가
            else:
                if r_floating_ban:
                    r_floating_ban -= 1  # Radiant 당에 대한 금지 횟수 감소
                    r_count -= 1  # Radiant 당 상원의원 수 감소
                else:
                    d_floating_ban += 1  # Dire 당에 대한 금지 횟수 증가
                    q.append('R')  # Radiant 상원의원을 다시 큐에 추가

        # 남아 있는 상원의원이 있는 당을 반환
        return 'Radiant' if r_count else 'Dire'
```