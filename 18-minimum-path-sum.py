from copy import deepcopy

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        D = deepcopy(grid)
        for i in range(m):
            for j in range(n):
                l = []
                if i > 0:
                    l.append(D[i - 1][j])
                if j > 0:
                    l.append(D[i][j - 1])
                if len(l) > 0:
                    D[i][j] += min(l)
        return D[-1][-1]
        
