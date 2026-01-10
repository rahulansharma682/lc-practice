class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for r in range(9):
            seen = set()
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        
        for c in range(9):
            seen = set()
            for r in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        for br in range(0,9,3):
            for bc in range(0,9,3):
                box = set()
                for r in range(br, br+3):
                    for c in range(bc, bc+3):
                        val = board[r][c]
                        if val == ".":
                            continue
                        if val in box:
                            return False
                        box.add(val)
        
        return True     