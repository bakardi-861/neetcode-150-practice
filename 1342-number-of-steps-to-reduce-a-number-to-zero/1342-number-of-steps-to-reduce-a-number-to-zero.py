class Solution:
    def numberOfSteps(self, num: int) -> int:
        ops = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            ops += 1
        return ops