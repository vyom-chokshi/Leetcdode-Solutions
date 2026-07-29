class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=[]
        r=[]
        for i in nums:
            if i%2!=0:
               l.append(i)
            else:
               r.append(i)
        r.extend(l)
        return r