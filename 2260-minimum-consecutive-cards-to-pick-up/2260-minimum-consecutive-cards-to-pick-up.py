class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
       # cards = [2,4,7,3,7]
       # expand window until dupe found, then shrink left until cards[l] == cards[r], then get the length.
       # repeat until array processed
        win = {}
        l = 0
        res = float("inf")
        for r in range(len(cards)):
            if cards[r] in win:
                res = min(res, r-win[cards[r]]+1)
            win[cards[r]] = r
        return res if res != float("inf") else -1

