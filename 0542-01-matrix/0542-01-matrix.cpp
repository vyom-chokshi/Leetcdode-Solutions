class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) 
    {
        int row=mat.size();
        int col=mat[0].size();
        queue<pair<int,int>> q;
        vector<vector<bool>> visited(row,vector<bool>(col,false));
        for(int i=0;i<row;i++)  
        {
            for(int j=0;j<col;j++)
            {
                if(mat[i][j]==0)
                {
                    q.push({i,j});
                    visited[i][j]=true;
                }
            }
        } 
       
        int dr[]={1,-1,0,0};
        int dc[]={0,0,-1,1};

        while(!q.empty())
        {
            auto temp=q.front();
            q.pop();
            int nr=temp.first;
            int nc=temp.second;

           
            for(int i=0;i<4;i++)
            {
                int r=nr+dr[i];
                int c=nc+dc[i];

                if(r>=0 && r<row && c>=0 && c<col && !visited[r][c])
                {
                    visited[r][c]=true;
                    mat[r][c] = mat[nr][nc] + 1;
                    q.push({r,c});

                }
            }


        }
        return mat;
    }
};