class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        win = defaultdict(int)
        res = []
        l = 0
        for r in range(len(s)):
            win[s[r]] += 1
            if r-l+1 > len(p):
                win[s[l]] -= 1
                if win[s[l]] == 0:
                    del win[s[l]]
                l += 1

            if win == p_count:
                res.append(l)
        return res    