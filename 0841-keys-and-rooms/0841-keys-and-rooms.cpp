class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) 
    {
        int n=rooms.size();
        stack<int> s;
        vector<int>visited(n,false);
        s.push(0);
        visited[0]=true;
        while(!s.empty())
        {
            int temp=s.top();
            s.pop();
            for(auto x:rooms[temp])
            {
                if(!visited[x])
                {
                    visited[x]=true;
                    s.push(x);
                }
            }
        }
        for(int i=0;i<n;i++)
        {
            if(!visited[i])
            {
                return false;
            }
        }
        return true;
    }
};