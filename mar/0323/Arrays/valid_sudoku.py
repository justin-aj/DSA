# Valid Sudoku
# Pattern: HashSet (rows, cols, boxes)
# Difficulty: Medium
# Frequency: Low for Amazon intern (more common at Google/Meta)

from collections import defaultdict

def isValidSudoku(board):
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)  # key = (row//3, col//3)

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.': continue

            # check row, col, box simultaneously
            if (val in rows[r] or
                val in cols[c] or
                val in boxes[(r//3, c//3)]):
                return False

            rows[r].add(val)
            cols[c].add(val)
            boxes[(r//3, c//3)].add(val)

    return True

# Key trick: (r//3, c//3) maps each cell to one of 9 boxes
# Time: O(81) = O(1) — fixed 9x9 grid
# Space: O(81) = O(1)
