class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            x=set()
            for j in range(1,floor(sqrt(i)) + 1):
                if i%j==0:
                    x.add(j)
                    x.add(i//j)
                if len(x)>4:
                    break
            if len(x)==4:
                res+=sum(x)
        return res