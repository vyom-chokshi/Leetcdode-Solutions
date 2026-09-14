class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans=[]
        for i in tokens:

            if i=="+":
                a=ans.pop()
                b=ans.pop()
                ans.append(a+b)

            elif i=="-":
                a=ans.pop()
                b=ans.pop()
                ans.append(b-a)
            
            elif i=="/":
                a=ans.pop()
                b=ans.pop()
                ans.append(int(b/a))
            
            elif i=="*":
                a=ans.pop()
                b=ans.pop()
                ans.append(a*b)
            
            else:    
            
                ans.append(int(i))

        return ans[-1]