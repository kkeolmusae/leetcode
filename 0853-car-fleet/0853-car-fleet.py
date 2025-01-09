class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed))  # 자동차 위치랑 속도 묶고 내림차순

        # target에 도달하는데 걸리는 시간 (오름차순으로 되어있음)
        times = [float(target - p) / s for p, s in cars]
        ans = 0

        while len(times) > 1:
            curr = times.pop()  # 제일 빨리 target에 도착하는 차

            # times[-1]: 그 다음으로 도착하는 차
            if times[-1] > curr:  # 못따라잡음
                ans += 1
            else:
                times[-1] = curr  # 합류
        return ans + len(times)