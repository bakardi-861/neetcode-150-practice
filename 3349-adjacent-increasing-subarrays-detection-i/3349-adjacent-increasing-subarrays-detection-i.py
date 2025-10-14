class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        curr_len = 1          # length of current increasing run
        prev_len = 0          # length of previous increasing run
        max_pair_len = 0      # max combined "paired" increasing pattern found

        # [1,2,3,0,2,4]
        #            i
        # curr = 3
        # prev =  3
        # max = 3

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_len += 1
            else:
                prev_len = curr_len  # store previous run before breaking
                curr_len = 1         # reset current run length

            # check the best combo:
            # - curr_len // 2 handles a single long increasing run
            # - min(prev_len, curr_len) handles two consecutive runs
            max_pair_len = max(max_pair_len, max(curr_len // 2, min(prev_len, curr_len)))

            if max_pair_len >= k:
                return True
        return False