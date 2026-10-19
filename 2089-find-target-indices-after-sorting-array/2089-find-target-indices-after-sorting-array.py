class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        x=sorted(nums)
        i=0
        l=[]
        for i in range(len(x)):
            if x[i]==target:
                l.append(i)
            elif x[i]>target:
                break
        return l
