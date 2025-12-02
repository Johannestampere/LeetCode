class Solution(object):
    def orangesRotting(self, grid):
        # BFS on multiple oranges at a time - O(m*n)

        m, n = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0, 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append([row, col])
        
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft() # get the coords of the rotten orange
                for dr, dc in dirs:
                    row, col = r + dr, c + dc
                    if row < 0 or row == m or col < 0 or col == n or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1