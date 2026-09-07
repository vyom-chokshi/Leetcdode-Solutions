class Solution {
public:

    int ans(int n,vector<int> &dp)
    {
        if(n==0 || n==1)
        return 1;

        else if(n==2)
        return 2;

        if(dp[n]!=-1)
        return dp[n];

        dp[n]=ans(n-1,dp)+ans(n-2,dp);
        return dp[n];   
    }     
    int climbStairs(int n) {
        vector<int> dp(n+1,-1);
        return ans(n,dp);
    }
};