class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # candidate = None
        count = 0
        max_count = 0

        for i,n in enumerate(nums):
            if i > 0 and n > nums[i-1]:
                count = 0
                
            count += 1
            max_count = max(max_count,count)

            if max_count > (len(nums) // 2) and n == target:
                return True
        return False