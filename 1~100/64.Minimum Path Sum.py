class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0]) if grid else 0
        for row in range(rows):
            for col in range(cols):
                if row > 0 and col > 0:
                    res = min(grid[row - 1][col],
                              grid[row][col - 1])
                elif row > 0:
                    res = grid[row - 1][col]
                elif col > 0:
                    res = grid[row][col - 1]
                else:
                    res = 0
                grid[row][col] += res
        return grid[-1][-1]
