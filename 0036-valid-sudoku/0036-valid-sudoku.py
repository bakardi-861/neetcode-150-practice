class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each row must contain the digits 1-9 without repetition.
        # Each col must contain the digits 1-9 without repetition.
        # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        # A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        # Only the filled cells need to be validated according to the mentioned rules.
        # WE DON'T NEED TO SOLVE, ONLY VALIDATE CURRENT BOARD STATE

        # create a set for each row and col, and sub box to store each digit.
        # 3x3 box index: box_index = (row // 3, col // 3)


        seen = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                # create keys
                row_key = ("row", r, val)
                col_key = ("col", c, val)
                box_key = ("box", r // 3, c // 3, val)
                
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
        return True