class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # fisherman cant move to land cells
        # can only start at water cells
        # DFS each water cell to find max sum of water cells (island)?


        # num islands pattern - DFS
        # rotting oranges pattern - BFS
        rows,cols = len(grid),len(grid[0])
        def dfs(r,c):
            if min(r,c) < 0 or r >= rows or c >= cols or grid[r][c] == -1 or grid[r][c] == 0:
                return 0
            
            fish = grid[r][c]
            grid[r][c] = -1

            max_sum = 0
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                max_sum += dfs(r+dr, c+dc)
            return max_sum + fish

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    res = max(res, dfs(r,c))
        return res
