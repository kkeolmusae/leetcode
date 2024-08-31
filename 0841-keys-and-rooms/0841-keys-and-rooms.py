class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = []
        q.extend(rooms[0])

        visited_room = [0] * len(rooms)
        visited_room[0] = 1  # 첫번째 방은 방문함

        while q:
            key = q.pop()  # 내가 보유한 열쇠
            if visited_room[key] == 0:  # 방문한 적 없으면
                q.extend(rooms[key])
                visited_room[key] = 1  # 방문처리
        if sum(visited_room) == len(rooms):
            return True
        return False