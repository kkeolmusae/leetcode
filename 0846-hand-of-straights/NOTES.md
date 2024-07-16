# 다른 풀이

### 내 풀이
나는 이렇게 품. 숫자-개수 별로 count 만들어서 q배열에 제일 작은거 하나씩 넣어가면서 마지막에 넣은 값이랑 연속되면 넘어가고, 만약에 아니면 False 리턴하는 방식으로. 근데 `min(count.keys())` 랑 while 문이랑 중첩되면서 Time complexity가 최악의 경우에 `O(n^2)` 이 됨. 약간 비효율적임
```py
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        count = Counter(hand)

        q = []
        while count:
            if not q:
                item = min(count.keys())
                q.append(item)
                if count[item] == 1:
                    del count[item]
                else:
                    count[item] = count[item] - 1
            else:
                next_num = q[-1] + 1
                if not count[next_num]:
                    return False
                else:
                    q.append(next_num)
                    if count[next_num] == 1:
                        del count[next_num]
                    else:
                        count[next_num] = count[next_num] - 1

            if len(q) == groupSize:
                print(q)
                q = []

        if q:
            return False
        return True
```

### 다른 풀이 1
- 시간 복잡도: `𝑂(𝑛⋅log𝑛+𝑛⋅𝑘)` 

heapq 랑 Count 쓴 방법. heapq 쓰면 `min(count.keys())` 이거 안써도 되서 시간 복잡도가 줄어듬
O(n⋅logn+n⋅k)


```py
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand_size = len(hand)

        if hand_size % groupSize != 0:
            return False

        # Counter to store the count of each card value
        card_count = Counter(hand)

        # Min-heap to process the cards in sorted order
        min_heap = list(card_count.keys())
        heapq.heapify(min_heap)

        # Process the cards until the heap is empty
        while min_heap:
            current_card = min_heap[0]  # Get the smallest card value
            # Check each consecutive sequence of groupSize cards
            for i in range(groupSize):
                if card_count[current_card + i] == 0:
                    return False
                card_count[current_card + i] -= 1
                if card_count[current_card + i] == 0:
                    if current_card + i != heapq.heappop(min_heap):
                        return False

        return True
```

### 다른 풀이 2
- 시간복잡도: `O(nlogn+n)`
```py
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Map to store the count of each card value
        cardCount = defaultdict(int)
        for card in hand:
            cardCount[card] += 1

        # Sorted list of card values
        sortedCards = sorted(cardCount.keys())
        # Queue to keep track of the number of new groups
        # starting with each card value
        groupStartQueue = deque()
        lastCard = -1
        currentOpenGroups = 0

        for currentCard in sortedCards:
            # Check if there are any discrepancies in the sequence
            # or more groups are required than available cards
            if (
                currentOpenGroups > 0 and currentCard > lastCard + 1
            ) or currentOpenGroups > cardCount[currentCard]:
                return False

            # Calculate the number of new groups starting
            # with the current card
            groupStartQueue.append(cardCount[currentCard] - currentOpenGroups)
            lastCard = currentCard
            currentOpenGroups = cardCount[currentCard]

            # Maintain the queue size to be equal to groupSize
            if len(groupStartQueue) == groupSize:
                currentOpenGroups -= groupStartQueue.popleft()

        # All groups should be completed by the end
        return currentOpenGroups == 0
```

### 다른 풀이 3
- 시간복잡도: `O(n)`
```py
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # Counter to store the count of each card value
        card_count = Counter(hand)

        for card in hand:
            start_card = card
            # Find the start of the potential straight sequence
            while card_count[start_card - 1]:
                start_card -= 1

            # Process the sequence starting from start_card
            while start_card <= card:
                while card_count[start_card]:
                    # Check if we can form a consecutive sequence
                    # of groupSize cards
                    for next_card in range(start_card, start_card + groupSize):
                        if not card_count[next_card]:
                            return False
                        card_count[next_card] -= 1
                start_card += 1

        return True
```