class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # circular: index + n
        # want to make sure gas stays >= 0
        # Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
        #                     s
        #               i                   i
        # steps: 
        # s = start index
        # gas = 0 to start
        # if gas + gas[i] - cost[i] < 0: route is invalid, increment s and reset i = s
        # else, route starting at s is valid so we can continue the loop

     
        n = len(gas)

        for start in range(n):
            tank = 0
            i = start
            completed = True

            while True:
                tank += gas[i] - cost[i]
                if tank < 0:
                    completed = False
                    break
                i = (i + 1) % n
                if i == start:
                    break

            if completed:
                return start

        return -1

