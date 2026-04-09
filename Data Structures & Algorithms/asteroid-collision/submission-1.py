class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output = []
        for i in asteroids:
            output.append(i)
            while len(output) > 1 and output[-2] > 0 and output[-1] < 0:
                if abs(output[-1]) < abs(output[-2]):
                    output.pop()
                elif abs(output[-1]) > abs(output[-2]):
                    output.pop(-2)
                else:
                    output.pop()
                    output.pop()
        return output