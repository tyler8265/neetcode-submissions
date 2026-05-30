class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_seen = collections.defaultdict(set)
        cols_seen = collections.defaultdict(set)
        threebythree_seen = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                if val in rows_seen[r]:
                    return False
                if val in cols_seen[c]:
                    return False
                if val in threebythree_seen[(r//3, c//3)]:
                    return False
                rows_seen[r].add(val)
                cols_seen[c].add(val)
                threebythree_seen[(r//3, c//3)].add(val)
        return True