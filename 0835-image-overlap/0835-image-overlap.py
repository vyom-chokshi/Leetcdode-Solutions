class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        im1=[]
        im2=[]
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j]==1:
                    im1.append((i,j))
                if img2[i][j]==1:
                    im2.append((i,j))
        dic={}

        for i,j in im1:
            for x,y in im2:
                dx=i-x
                dy=j-y

                dic[(dx,dy)]=dic.get((dx,dy),0)+1
        
        return max(dic.values(),default=0)