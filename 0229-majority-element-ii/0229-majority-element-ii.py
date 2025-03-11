class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        def updateCount(counts, candidates,n,k):
            for i in range(k):
                if candidates[i] != None and candidates[i] == n:
                    counts[i] += 1
                    return True
            return False

        def populateCandidate(counts,candidates,n,k):
            if (updateCount(counts,candidates,n,k)):
                return

            for i in range(k):
                if counts[i] == 0:
                    candidates[i] = n
                    counts[i] += 1
                    return

            for i in range(k):
                counts[i] -= 1


        k = 3
        res = []
        if len(nums) <= k-1:
            return list(set(nums))
        
        counts = [0] * (k-1)
        candidates = [None] * (k-1)

        for n in nums:
            populateCandidate(counts,candidates,n,k-1)
        
        counts = [0] * (k-1)
        for n in nums:
            updateCount(counts,candidates,n,k-1)
        
        threshold = len(nums)/k
        for i in range(k-1):
            if counts[i] > threshold:
                res.append(candidates[i])
        return res

