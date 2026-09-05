class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) 
    {
        int n=nums.size();
        vector<int> prifix(n);
        vector<int> sufix(n);  
        
        prifix[0]=nums[0];
        sufix[n-1]=nums[n-1];
        for(int i=1;i<n;i++)
        {
            prifix[i]=max(prifix[i-1],nums[i]);
        } 
        for(int i=n-2;i>=0;i--)
        {
            sufix[i]=min(sufix[i+1],nums[i]);
        }
        int x;
        for(int i=0;i<n;i++)
        {
            x=prifix[i]-sufix[i];
            if(x<=k)
            {
                return i;
            }
        }

       return -1;
    }
};