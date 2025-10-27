class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        from collections import Counter

        coords = set(map(tuple, coordinates))
        counter = Counter()

        # For each black cell, find all top-left corners of 2x2 blocks it belongs to
        for r, c in coords:
            for dr in (-1, 0):
                for dc in (-1, 0):
                    nr, nc = r + dr, c + dc
                    # must be a valid top-left corner of a 2x2 block
                    if 0 <= nr < m - 1 and 0 <= nc < n - 1:
                        counter[(nr, nc)] += 1

        ans = [0] * 5
        for count in counter.values():
            ans[count] += 1

        total_blocks = (m - 1) * (n - 1)
        ans[0] = total_blocks - sum(ans[1:])

        return ans