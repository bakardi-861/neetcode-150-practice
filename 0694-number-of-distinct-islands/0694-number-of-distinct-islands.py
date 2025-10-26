class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # keep track of island size (distances of each cell to start cell)
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        rows,cols = len(grid),len(grid[0])
        visit = set()

        def dfs(r,c,start_r,start_c,island):
            if min(r,c) < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return
            
            grid[r][c] = 2
            island.append((r-start_r,c-start_c))

            for dr,dc in dirs:
                dfs(r+dr,c+dc,start_r,start_c,island)
            return island
            
        
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    island = tuple(dfs(r,c,r,c,[]))
                    if island not in visit:
                        islands += 1
                        visit.add(island)
        return islands