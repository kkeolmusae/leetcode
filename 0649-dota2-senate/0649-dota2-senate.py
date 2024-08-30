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
                if other in queue:
                    queue.remove(other)
            current_senator = curr  # 현재 상원 업데이트
            queue.append(curr)  # 제일 뒤 라운드로

            if (queue.count("R") or queue.count("D")) == len(queue):
                break
        return "Radiant" if current_senator == "R" else "Dire"