class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        dic={}
        for p,q in knowledge:
            dic[p]=q
        ans=""
        i=0
        while i!=len(s):
            if s[i]=='(':
                j=i+1
                y=""
            
                while s[j]!=")":
                    y+=s[j]
                    j+=1
                i=j+1
                
                ans+=dic.get(y,"?") 
               
            else:
                ans+=s[i]
                i+=1
        return ans