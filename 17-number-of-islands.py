class Solution(object):
    def color(self, grid, i, j):
        q = deque([(i, j)])
        while len(q) > 0:
            i, j = q.popleft()
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or \
                (grid[i][j] == '0'):
                continue
            grid[i][j] = '0'
            q.append((i + 1, j))
            q.append((i - 1, j))
            q.append((i, j + 1))
            q.append((i, j - 1))
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.color(grid, i,j)
                    count += 1
        return count
