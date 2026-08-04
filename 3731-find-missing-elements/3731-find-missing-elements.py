class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums=sorted(nums)
        s=set(nums)
        num=[]
        mn=nums[0]
        ma=nums[-1]
        for i in range(mn,ma):
            if i not in s:
                num.append(i)
        return num