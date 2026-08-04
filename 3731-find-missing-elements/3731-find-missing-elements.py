class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums=sorted(nums)
        num=[]
        for i in range(nums[0],nums[-1]):
            if i not in nums:
                num.append(i)
        return num