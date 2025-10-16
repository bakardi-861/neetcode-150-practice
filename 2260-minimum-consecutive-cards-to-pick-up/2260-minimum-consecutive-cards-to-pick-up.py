class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
       # cards = [2,4,7,3,7]
       # expand window until dupe found, then shrink left until cards[l] == cards[r], then get the length.
       # repeat until array processed
        win = Counter()
        l = 0
        res = float("inf")
        for r in range(len(cards)):
            win[cards[r]] += 1
            while len(win) < r-l+1:
                res = min(res,r-l+1)
                win[cards[l]] -= 1
                if not win[cards[l]]: del win[cards[l]]
                l += 1
        return res if res != float("inf") else -1

