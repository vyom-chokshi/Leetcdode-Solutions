class Solution {
public:
    int missingMultiple(vector<int>& nums, int k) 
    {
        set<int> num(nums.begin(),nums.end());
        int x=k;
        while(num.find(x)!=num.end())
        {
            x+=k;
        }
        return x;
    }
};