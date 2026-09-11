class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int i=-1;
        
        for(i=nums.size()-2;i>=0;i--)
        {
            if(nums[i]<nums[i+1])
            {
                break;
            }
        }
        if(i==-1)
        {
            reverse(nums.begin(),nums.end());
            return;
        }
        for(int j=nums.size()-1;j>i;j--)
        {
            if(nums[i]<nums[j])
            {
                swap(nums[i],nums[j]);

                break;
            }
        }
        reverse(nums.begin()+i+1,nums.end());      

    }
};