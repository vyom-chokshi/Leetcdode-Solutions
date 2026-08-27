class Solution {
public:

    void dfs(vector<vector<char>>& grid,int i, int j)
    {
        if(i<0 || j<0 || i>=grid.size() || j>=grid[0].size())
        {
            return;
        }

        if(grid[i][j]=='V' || grid[i][j]=='X')
        {
            return;
        }

        grid[i][j]='V';

        dfs(grid,i+1,j);
        dfs(grid,i-1,j);
        dfs(grid,i,j-1);
        dfs(grid,i,j+1);
    }

    void solve(vector<vector<char>>& board) 
    {
        int row=board.size();
        int col=board[0].size();
        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {

                if(board[i][j]=='O')
                {
                  if(i==row-1 || j==col-1 || i== 0 || j==0)
                  {
                    dfs(board,i,j);
                  }
                  
                }
            }
        }

        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {
                if(board[i][j]=='O')
                {
                    board[i][j]='X';
                }
            }

        } 

        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {
                if(board[i][j]=='V')
                {
                    board[i][j]='O';
                }
            }

        } 
        
    }
};