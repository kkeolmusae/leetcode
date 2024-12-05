class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        curr = 0
        result = 0

        for idx in range(len(gas)):
            used_gas = gas[idx] - cost[idx]
            total += used_gas
            curr += used_gas

            # curr 이 음수면 다음 지역으로 못간다는거임
            if curr < 0:
                curr = 0  # 초기화하고
                result = idx + 1  # 현재 위치에서는 안되는거니깐 다음 위치로 설정

        if total >= 0:  # total이 양수면 모든 지역 다 갈 수 있다는거임
            return result
        return -1
