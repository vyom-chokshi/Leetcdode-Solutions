class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) 
    {
        int n=nums.size();
        
        vector<int> sufix(n);  
        
       
        sufix[n-1]=nums[n-1];
        
        for(int i=n-2;i>=0;i--)
        {
            sufix[i]=min(sufix[i+1],nums[i]);
        }
        int x;
        int prifix=nums[0];
        for(int i=0;i<n;i++)
        {
            prifix=max(prifix,nums[i]);
            x=prifix-sufix[i];
            if(x<=k)
            {
                return i;
            }
        }

       return -1;
    }
};