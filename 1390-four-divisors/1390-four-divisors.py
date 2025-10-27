class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            divisors = set()
            for dividend in range(1,floor(sqrt(num)) + 1):
                if num % dividend == 0:
                    divisors.add(dividend)
                    divisors.add(num // dividend)
                if len(divisors) > 4:
                    break
            if len(divisors) == 4:
                res += sum(divisors)
        return res