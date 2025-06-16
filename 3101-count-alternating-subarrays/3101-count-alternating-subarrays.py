class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        total = 0
        
        for right in range(n):
            # If not the first element and current equals previous, move left pointer
            if right > 0 and nums[right] == nums[right - 1]:
                left = right
            
            # Count subarrays ending at right
            total += (right - left + 1)
        
        return total
