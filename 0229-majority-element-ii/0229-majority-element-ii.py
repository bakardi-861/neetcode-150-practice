class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # same as majority element 1, but just seeing if it appears n//3 times?
        # is B.M. only useful when we have the n // 2 condition?
        
        counter = Counter(nums)
        return [c for c in counter if counter[c] > len(nums)//3]

