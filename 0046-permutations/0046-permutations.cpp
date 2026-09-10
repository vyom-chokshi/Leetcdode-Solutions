class Solution {
public:
    void per(vector<int>&n,int index,vector<vector<int>>&ans)
    {
        if(index==n.size())
        {
            ans.push_back(n);
        }
        for(int i=index;i<n.size();i++)
        {
            swap(n[index],n[i]);
            per(n,index+1,ans);
            swap(n[index],n[i]);
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        per(nums,0,ans);
        return ans;
    }
};