class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        times = n // 2
        count = 0

        counter = Counter(nums)
        for c in counter:
            if counter[c] > times:
                return c
        return -1
        
        # for num in nums:
        #     # count += 1
        #     # if count > times:
        #     #     return num
        # return -1 # will never get here bc majority element always exists