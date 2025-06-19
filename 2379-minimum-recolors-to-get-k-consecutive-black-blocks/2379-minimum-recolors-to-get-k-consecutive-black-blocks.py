class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        win = Counter(blocks[:k])
        min_ops = min(float("inf"),win["W"])
        for i in range(k,len(blocks)):
            win[blocks[i]] += 1
            win[blocks[i-k]] -= 1
            min_ops = min(min_ops,win["W"])
        return min_ops