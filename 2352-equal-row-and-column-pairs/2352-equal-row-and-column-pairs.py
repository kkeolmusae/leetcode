class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        height_list = [] # 세로 목록 저장
        cnt = 0
        for i in range(n):

            height = []
            for j in range(n):
                height.append(grid[j][i])
            height_list.append(height)

        for i in range(n):
            for j in range(n):
                if height_list[i] == grid[j]:  # 세로랑 가로랑 비교해서 같으면 cnt += 1
                    cnt += 1
        return cnt