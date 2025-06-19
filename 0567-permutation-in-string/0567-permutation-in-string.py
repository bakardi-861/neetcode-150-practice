class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 = "ab", s2 = "eidboaoo"
        # win = {o:2}
        # s1_count = {a:1,b:1}

        s1_count = Counter(s1)
        l = 0
        win = defaultdict(int)
        for r in range(len(s2)):
            win[s2[r]] += 1
            if r-l+1 > len(s1):
                win[s2[l]] -= 1
                if win[s2[l]] == 0: del win[s2[l]]
                l += 1

            if win == s1_count:
                return True
        return False