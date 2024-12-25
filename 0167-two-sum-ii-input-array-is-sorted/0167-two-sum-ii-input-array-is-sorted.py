class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lidx = 0
        ridx = len(numbers) - 1

        while True:
            x = numbers[lidx]
            y = numbers[ridx]

            if x + y == target:  # 숫자가 target이랑 같으면 끝
                return [lidx + 1, ridx + 1]

            if x + y > target:
                # 숫자 합친게 target 보다 크면 오른쪽 인덱스를 왼쪽으로 이동
                ridx -= 1
            else:
                # 숫자 합친게 target 보다 작으면 왼쪽 인덱스를 오른쪽으로 이동
                lidx += 1