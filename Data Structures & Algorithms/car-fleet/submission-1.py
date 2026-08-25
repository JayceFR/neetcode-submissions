class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        if len(position) <= 1:
            return len(position)

        # (pos, time)
        cars = []
        for x in range(len(position)):
            cars.append((position[x], speed[x]))
        
        cars.sort(reverse = True)
        rp = 1
        timeToTarget = (target - cars[0][0]) / cars[0][1]
        while rp != len(cars):
            # print(int((target - cars[rp][0]) / cars[rp][1]), timeToTarget)
            if (target - cars[rp][0]) / cars[rp][1] <= timeToTarget:
                cars.pop(rp)
            else:
                timeToTarget = (target - cars[rp][0]) / cars[rp][1]
                rp += 1

        return len(cars)