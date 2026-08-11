class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sm=nums[0]
        n=len(nums)
        for i in range(1,n):
            if nums[i] == nums[i-1]+1:
                sm+=nums[i]
            else :
                break
        while sm in nums:
           sm+=1
        return sm 