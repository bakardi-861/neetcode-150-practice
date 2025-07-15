class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n

        doubled = code * 2
        res = []

        if k > 0:
            for i in range(n):
                res.append(sum(doubled[i+1:i+k+1]))
        else:
            for i in range(n):
                res.append(sum(doubled[i+n+k:i+n]))

        return res
