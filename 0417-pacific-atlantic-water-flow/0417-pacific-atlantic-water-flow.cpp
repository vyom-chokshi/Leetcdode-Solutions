class Solution {
public:
    void dfs(vector<vector<int>> &h,vector<vector<bool>> &visited,int i,int j)
    {
        if(i<0 || j<0 || i>=h.size() || j>=h[0].size())
        {
            return;
        }
        if(visited[i][j])
        {
            return;
        }
        visited[i][j]=true;
        if(i-1>=0 && h[i-1][j]>=h[i][j])
        {
            dfs(h,visited,i-1,j);
        }
        if(i+1<h.size() && h[i+1][j]>=h[i][j])
        {
            dfs(h,visited,i+1,j);
        }
        if(j-1>=0 && h[i][j-1]>=h[i][j])
        {
            dfs(h,visited,i,j-1);
        }
        if(j+1<h[0].size() && h[i][j+1]>=h[i][j])
        {
            dfs(h,visited,i,j+1);
        }

    }
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) 
    {
        int row=heights.size();
        int col=heights[0].size();

        vector<vector<bool>>Pacific(row,vector<bool>(col,false));
        vector<vector<bool>>Atlantic(row,vector<bool>(col,false));

        for(int j = 0; j < col; j++)
        {
            dfs(heights, Pacific, 0, j);
        }

        for(int i = 0; i < row; i++)
        {
            dfs(heights, Pacific, i, 0);
        }

        for(int j = 0; j < col ; j++)
        {
            dfs(heights, Atlantic, row-1, j);
        }

        for(int i = 0; i < row; i++)
        {
            dfs(heights, Atlantic, i, col-1);
        }

        vector<vector<int>> ans;
        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {
                if(Atlantic[i][j] && Pacific[i][j])
                {ans.push_back({i,j});}
            }
        }
        return ans;
    }
};