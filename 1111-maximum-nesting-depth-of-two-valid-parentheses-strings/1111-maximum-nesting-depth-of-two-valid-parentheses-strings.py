class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        x=0
        l=[]
        for i in seq:
            if i=="(":
                x+=1
                l.append(x%2)
                
            else:
                
                l.append(x%2)
                x-=1
        return l