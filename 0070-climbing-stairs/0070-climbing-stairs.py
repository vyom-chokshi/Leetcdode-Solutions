class Solution:
    def climbStairs(self, n: int) -> int:
        dp={}
        def slove(n):
            if n==1:
                return 1
            if n==2:
                return 2
            if n in dp:
                return dp[n]
            dp[n]=slove(n-1)+slove(n-2)
            return dp[n]
        return slove(n)