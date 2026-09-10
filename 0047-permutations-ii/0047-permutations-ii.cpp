class Solution {
public:
void solve(vector<int>&n,int index,vector<vector<int>>&ans)
{
    if(index==n.size())
    {
        ans.push_back(n);
    }
    set<int> used;
    for(int i= index;i<n.size();i++)
    {
        if(used.count(n[i]))
            continue;
        used.insert(n[i]);
        swap(n[index],n[i]);
        solve(n,index+1,ans);
        swap(n[index],n[i]);
    }
}
    vector<vector<int>> permuteUnique(vector<int>& nums) {
     vector<vector<int>>ans;
     solve(nums,0,ans);
     return ans;   
    }
};