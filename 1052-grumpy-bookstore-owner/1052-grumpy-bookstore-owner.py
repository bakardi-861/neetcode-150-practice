class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base_satisfaction = 0
        # always count these customers as satisfied
        for i in range(len(customers)):
            if grumpy[i] == 0:
                base_satisfaction += customers[i]

        
        # for the first minutes long window, sum satisfied customers if grumpy
        boost = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                boost += customers[i]

        # starting at minutes to len(customers), add the new customer if grumpy and subtract the first customer
        # calculate the max each time
        max_boost = boost
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                boost += customers[i]
            if grumpy[i - minutes] == 1:
                boost -= customers[i - minutes]
            max_boost = max(max_boost, boost)
        return base_satisfaction + max_boost

