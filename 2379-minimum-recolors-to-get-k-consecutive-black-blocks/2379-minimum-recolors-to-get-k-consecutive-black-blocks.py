#from collections import defaultdict
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_ops = float("inf")
        l,r = 0,0
        win = defaultdict(int)
        for r in range(len(blocks)):
            win[blocks[r]] += 1
            # if win too big, shrink it
            if r-l+1 > k:
                win[blocks[l]] -= 1
                if win[blocks[l]] == 0: del win[blocks[l]]
                l += 1

            # if window size is k, get the min ops needed
            if r-l+1 == k:
                min_ops = min(win["W"],min_ops)
        return min_ops