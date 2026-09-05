class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        p = [0] * n
        s = [0] * n

    
        p[0] = nums[0]

        for i in range(1, n):
            p[i] = max(nums[i], p[i-1])

    
        s[n-1] = nums[n-1]

        for i in range(n-2, -1, -1):
            s[i] = min(nums[i], s[i+1])

        
        for i in range(n):
            x = p[i] - s[i]

            if x <= k:
                return i

        return -1