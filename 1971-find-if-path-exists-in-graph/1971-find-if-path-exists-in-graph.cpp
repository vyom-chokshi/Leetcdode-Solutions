#include <stack>
class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
    

        vector<vector<int>> graph(n);
        for (auto edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        stack<int>s;
        vector<bool>visited(n,false);
        visited[source]=true;
        s.push(source);
        int temp;
        while(!s.empty())
        {
            temp=s.top();
            s.pop();
            if(temp==destination)
            return true;

            for(int x : graph[temp])
            {
                if(!visited[x])
                {
                    visited[x]=true;
                    s.push(x);
                }
            }
        }
    return false;   
    }

};