class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            r = num % k
            new_dp = [0] * k

            
            new_dp[r] += 1

           
            for mod in range(k):
                if dp[mod]:
                    new_mod = (mod * r) % k
                    new_dp[new_mod] += dp[mod]

           
            for mod in range(k):
                ans[mod] += new_dp[mod]

            dp = new_dp

        return ans