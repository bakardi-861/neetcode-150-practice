class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        win = Counter()
        l = 0
        k = len(s1)
        for r in range(len(s2)):
            win[s2[r]] += 1
            if r-l+1 > k:
                win[s2[l]] -= 1
                if not win[s2[l]]:
                    del win[s2[l]]
                l += 1
            if r-l+1 == k and win == s1_count:
                    return True
        return False

