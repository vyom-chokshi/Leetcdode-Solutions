class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        ans=-1
        n=len(nums)
        for i in range(n):
            ans=max(nums[0:i+1])-min(nums[i:n])
       
            if ans<=k:
                return i
        
        return -1
