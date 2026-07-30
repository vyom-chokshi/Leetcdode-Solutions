class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        num=sorted(nums)
        close=sum(num[:3])
        for i in range(len(num)):
            l=i+1
            r=len(num)-1
            while l<r:
                sm=num[i]+num[l]+num[r]
                if abs(sm - target) < abs(close - target):
                    close = sm
                if sm<target:
                    l+=1
                elif sm>target:
                    r-=1
                else:
                    return sm
        return close