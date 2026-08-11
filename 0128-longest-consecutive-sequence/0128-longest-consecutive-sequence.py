class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=0:
            return 0
        elif len(nums)==1:
            return 1
        num=sorted(nums)
       
        n=len(nums)
        x=1
        ans=1
        for i in range(1,n):
            if num[i]==num[i-1]+1:
                x+=1
            elif num[i]==num[i-1]:
                continue
            else:                
                x=1
            ans=max(ans,x)
            
        return ans
       