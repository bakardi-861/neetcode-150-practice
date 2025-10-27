class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divisors(x):
            res = set()
            for i in range(1, int(x**0.5) + 1):
                if x % i == 0:
                    res.add(i)
                    res.add(x // i)
            return sorted(res)

        res = 0
        for n in nums:
            divs = divisors(n)
            if len(divs) == 4:
                res += sum(divs)
        return res
