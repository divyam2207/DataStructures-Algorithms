class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_loc = []

        ROWS, COLS = len(matrix), len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zero_loc.append((r,c))
        
        for r,c in zero_loc:
            matrix[r] = [0] * COLS
            for i in range(0, ROWS):
                matrix[i][c] = 0
        
        return matrix