# O(m x n)

class Solution(object):
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])

        # marks entire visited land as water (0-s)
        def dfs(i, j):
            # check out of bounds or pos is not land
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return
            else:
                grid[i][j] = "0"
                # do the same for up, down, left, right to delete the island
                dfs(i, j + 1)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i - 1, j)
                

        n_islands = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    n_islands += 1
                    # cant double count
                    dfs(i, j)

        return n_islands