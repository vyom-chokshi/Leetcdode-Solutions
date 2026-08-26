class Solution {
public:
    int missingMultiple(vector<int>& nums, int k) 
    {
        unordered_set<int> num(nums.begin(),nums.end());
        int x=k;
        while(num.find(x)!=num.end())
        {
            x+=k;
        }
        return x;
    }
};