class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st=[]
        ts=[]
        for i in s:
            
            if i=="#":
                if st:
                    st.pop()
            else:
                st.append(i)
                
            

        for j in t:            
            if j=="#":
                if ts:
                    ts.pop()
            else:
                ts.append(j)
                
                

        return st==ts