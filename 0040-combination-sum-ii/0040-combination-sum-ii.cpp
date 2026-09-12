class Solution {
public:
    void back(vector<int>&can,vector<int>&count,int tar, vector<vector<int>>&result,int index)
        {
            if(tar==0)
            {
                result.push_back(count);
                return;
            }
            if(tar<0)
            {
                return;
            }
            for(int i=index;i<can.size();i++)
            {
                if (i > index && can[i] == can[i - 1])
                continue;

                count.push_back(can[i]);
                back(can,count,tar-can[i],result,i+1);
                count.pop_back();
            }

        }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>>result;
        
        sort(candidates.begin(), candidates.end());
        vector<int>count;
        back(candidates,count,target,result,0);
        return result;
    }
};