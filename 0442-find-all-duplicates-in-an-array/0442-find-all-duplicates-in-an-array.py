class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        num=sorted(nums)
        l=[]
        for i in range(len(num)-1):
            if num[i]==num[i+1]:
                l.append(num[i])
        return l