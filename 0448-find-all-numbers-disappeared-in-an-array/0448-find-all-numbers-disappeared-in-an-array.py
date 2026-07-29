class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=[]
        num=set(nums)
        for i in range(1,len(nums)+1):
            if i  not in num:
                l.append(i)
        return l
