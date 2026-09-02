class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        even=0
        odd=0
        for i in nums1:
            if i%2==0:
                even+=1
            elif i%2!=0:
                odd+=1
        if even==odd:
            return True
        elif even!=odd:
            return True