class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def collision(q, asteriod):
            if not q or q[-1] < 0:  # q가 비어있거나 기존값이 음수면 그냥 넣음
                q.append(asteroid)
            else:
                prev_asteriod = q[-1]

                if asteroid + prev_asteriod == 0:  # 두 행성 크기가 같으면
                    q.pop()  # 원래 있던 행성 폭팔
                    # 두 행성 크기가 다른데 부호가 같으면
                elif asteroid * prev_asteriod > 0:
                    q.append(asteroid)  # 그대로 추가
                else:  # 두 행성의 크기가 다른데 절대값이 다르면
                    # 새로들어온게 크면서 음수인 경우 충돌하면서 원래꺼 터짐
                    if abs(prev_asteriod) < abs(asteroid):
                        q.pop()  # 원래 있던 행성 폭팔
                        collision(q, asteriod)  # 재귀

        q = []
        for asteroid in asteroids:
            collision(q, asteroid)
        return q