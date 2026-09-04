class Solution {
public:
    int maxi(int end,vector<int>&nums)
    {
        int m=nums[0];
        for(int i=0;i<end;i++)
        {
            m=max(m,nums[i]);
        }
        return m;
    }

    int mini(int start,vector<int>&nums)
    {
        int m=nums[start];
        for(int i=start;i<nums.size();i++)
        {
            m=min(m,nums[i]);
        }
        return m;
    }

    int firstStableIndex(vector<int>& nums, int k) 
    {
        int ans=-1;
        int n=nums.size();
        for(int i=0;i<n;i++)
        {
            ans = maxi(i + 1,nums) - mini(i,nums);

            if(ans<=k)
            {
                return i;
            }
        }  
         return -1;

    }
};