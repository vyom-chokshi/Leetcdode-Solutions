class Solution {
public:
void solve(vector<int>&n,int index,set<vector<int>>&ans)
{
    if(index==n.size())
    {
        ans.insert(n);
    }

    for(int i= index;i<n.size();i++)
    {
        swap(n[index],n[i]);
        solve(n,index+1,ans);
        swap(n[index],n[i]);
    }
}
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        set<vector<int>>ans;
        solve(nums,0,ans);
        vector<vector<int>> result(ans.begin(), ans.end());

        return result;
    }
};