class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #  01234567
        # "abcabcbb"
        #     r
        #   l
        # win = {a:4,b:1,c:2}
        # l = 4
        # r = 2
        # max = 4

        
        win = {}
        l, max_len = 0,0
        for r, char in enumerate(s):
            if char in win:
                l = max(win[char] + 1, l)
            win[char] = r
            max_len = max(r-l+1,max_len)
        return max_len