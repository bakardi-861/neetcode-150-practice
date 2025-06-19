class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # window size = 2
        # longest substring with 2 unique characters
        l = 0
        win = defaultdict(int)
        longest = 0
        for r in range(len(fruits)):
            win[fruits[r]] += 1
            while len(win) > 2:
                win[fruits[l]] -= 1
                if win[fruits[l]] == 0: del win[fruits[l]]
                l += 1
            longest = max(longest, r-l+1)
        return longest

