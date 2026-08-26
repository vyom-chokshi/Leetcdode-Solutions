class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num=set(nums)
        x=k
        while x in num:
            x+=k
            
        return x









