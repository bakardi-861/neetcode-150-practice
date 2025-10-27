class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # operation = if num1 >= num2, subtract num2 form num1. else subtract num1 from num2
        ops = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            ops += 1
        return ops