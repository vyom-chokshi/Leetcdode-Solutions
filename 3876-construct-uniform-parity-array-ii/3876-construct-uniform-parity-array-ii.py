class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        x=min(nums1)
        if x%2!=0 :
            return True
        return all(y%2==0 for y in nums1 )