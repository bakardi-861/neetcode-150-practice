class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:
        # "." = not filled
        # each row must be a set of 1-9
        # each col must be a set of 1-9
        # each 3x3 box must be a set 1-9: get indices with r/3, c/3
        rows,cols = len(grid),len(grid[0])
        boxes = [set() for _ in range(10)]
        col_set = [set() for _ in range(10)]
        row_set = [set() for _ in range(10)]

        for r in range(rows):
            for c in range(cols):
                curr = grid[r][c]
                if curr == ".":
                    continue

                if curr in row_set[r] or curr in col_set[c] or curr in boxes[3*(r//3) + (c//3)]:
                    return False

                row_set[r].add(curr)
                col_set[c].add(curr)
                boxes[3*(r//3) + (c//3)].add(curr)
        return True
