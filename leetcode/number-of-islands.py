class Solution {
public:

    int m, n;
    vector<vector<char>>* gridPtr;

    void dfs(int i, int j) {
            if (i < 0 || i >= m || j < 0 || j >= n || (*gridPtr)[i][j] != '1') return;

            (*gridPtr)[i][j] = '0';

            dfs(i, j + 1);
            dfs(i + 1, j);
            dfs(i, j - 1);
            dfs(i - 1, j);
        }

    int numIslands(vector<vector<char>>& grid) {
                
        m = grid.size();
        n = grid[0].size();
        gridPtr = &grid;
        int count = 0;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '1') {
                    dfs(i, j);
                    ++count;
                }
            }
        }

        return count;

    }

    
};