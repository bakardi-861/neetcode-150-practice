class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        #  0123456
        # "abcabc"
        #       r
        #     l
        # win = {a:1,b:1,c:1}
        # # if win == chars # keys == "abc"
        #     ans += 1 + ((len(s)-1) - r)
        #     ans = 10

        
        win = {"a":0,"b":0,"c":0}
        l = 0
        ans = 0
        chars = set(["a","b","c"])
        for r in range(len(s)):
            win[s[r]] += 1
            while self.has_all_chars(win):
                ans += 1 + ((len(s)-1) - r)
                win[s[l]] -= 1
                l += 1
        return ans

    def has_all_chars(self,win:dict):
        return all(f > 0 for f in win.values())


