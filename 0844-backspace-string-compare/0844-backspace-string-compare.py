class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st=[]
        ts=[]
        for i in s:
            st.append(i)
            if i=="#":
                st.pop()
                if st!=[]:
                    st.pop()
            

        for j in t:
            ts.append(j)
            if j=="#":
                ts.pop()
                if ts!=[]:
                    ts.pop()
                

        return st==ts