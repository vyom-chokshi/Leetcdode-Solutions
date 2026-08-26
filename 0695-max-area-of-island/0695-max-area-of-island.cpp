class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) 
    {
        int row=grid.size();
        int col=grid[0].size();

      
        vector<vector<bool>>visited(row,vector<bool>(col,false));

       
        int ans=0;

        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {
                if(grid[i][j]==1&&!visited[i][j])
                {
                    int are=1;
                    visited[i][j]=true;
                    queue<pair<int,int>>q;
                    q.push({i,j});

                    while(!q.empty())
                    {
                        auto temp=q.front();
                        q.pop();

                        int dr[]={1,-1,0,0};
                        int dc[]={0,0,1,-1};

                        int r=temp.first;
                        int c=temp.second;

                        for(int x=0;x<4;x++)
                        {
                            int nr=r+dr[x];
                            int nc=c+dc[x];

                            if(nr<row && nc < col && nr>=0 && nc >=0 
                                && grid[nr][nc]==1 && !visited[nr][nc])
                                {
                                    visited[nr][nc]=true;
                                    q.push({nr,nc});
                                    are++;
                                }
                        }
                    }
                    ans=max(ans,are);
                    
                }
            }
        }
        return ans;
    }
};