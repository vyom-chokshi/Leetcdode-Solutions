class Solution {
public:
    bool search(vector<int>& nums, int target) 
    {
        int l=0;
        int m=nums.size()-1;
        while(l<=m)
        {
            int mid=(l+m)/2;

            if(nums[mid]==target)
            return true;

            if(nums[l] == nums[mid] && nums[mid] == nums[m])
            {
                l++;
                m--;
            }
            
             else if(nums[l] <= nums[mid])
            {
                if(nums[l] <= target && target < nums[mid])
                    m = mid - 1;
                else
                    l = mid + 1;
            }

            else
            {
                if(nums[mid] < target && target <= nums[m])
                    l = mid + 1;
                else
                    m = mid - 1;
            }

            
        }
        return false;
    }
};