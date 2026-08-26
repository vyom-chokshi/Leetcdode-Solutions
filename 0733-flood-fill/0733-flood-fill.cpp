class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) 
    {

        queue<pair<int,int>> q;
        vector<vector<bool>> visited(image.size(),vector<bool>(image[0].size(),false));

        
        int original = image[sr][sc];
        if (original == color)
            return image;

        q.push({sr,sc});

        visited[sr][sc]=true;
        image[sr][sc] = color;

        
        int dr[]={-1,1,0,0};
        int dc[]={0,0,-1,1};
        while(!q.empty())
        {
            auto temp=q.front();
            q.pop();
            int r=temp.first;
            int c=temp.second;
            for(int i=0;i<4;i++)
            {
               int nr=r+dr[i];
               int nc=c+dc[i];
               if(nc>=0 && nr<image.size()&& nr>=0 && nc<image[0].size()&& !visited[nr][nc] &&  image[nr][nc] == original)
               {
                visited[nr][nc]=true;
                image[nr][nc]=color;
                q.push({nr,nc});
               }
            }
        }  
        return image; 
    }
};