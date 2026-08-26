class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {

        int m = grid.size();
        int n = grid[0].size();

        vector<vector<bool>> visited(m, vector<bool>(n, false));

        int count = 0;

        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(grid[i][j] == '1' && !visited[i][j])
                {
                    count++;

                    queue<pair<int,int>> q;

                    q.push({i, j});
                    visited[i][j] = true;

                    while(!q.empty())
                    {
                        auto [r, c] = q.front();
                        q.pop();

                        int dr[] = {-1, 1, 0, 0};
                        int dc[] = {0, 0, -1, 1};

                        for(int k = 0; k < 4; k++)
                        {
                            int nr = r + dr[k];
                            int nc = c + dc[k];

                            if(nr >= 0 && nr < m &&
                               nc >= 0 && nc < n &&
                               grid[nr][nc] == '1' &&
                               !visited[nr][nc])
                            {
                                visited[nr][nc] = true;
                                q.push({nr, nc});
                            }
                        }
                    }
                }
            }
        }

        return count;
    }
};