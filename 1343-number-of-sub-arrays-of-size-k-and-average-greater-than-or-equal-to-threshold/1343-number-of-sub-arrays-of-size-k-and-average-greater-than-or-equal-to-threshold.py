class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        # nums = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
        #                    l
        #                      r
        # avg = sum / (r-l+1) = 6 res = 3
        
        # maintain fixed size window of size k
        # early terminate when len(win)-l < k
        res = 0
        l = 0
        win_sum = 0
        for r in range(len(nums)):
            win_sum += nums[r]

            # if too big, shrink it
            if r-l+1 > k:
                win_sum -= nums[l]
                l += 1
            
            # if avg >= threshold and window size == k
            avg = win_sum / (r-l+1)
            if avg >= threshold and r-l+1 == k:
                res += 1
        return res
            

