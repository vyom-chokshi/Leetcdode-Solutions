class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 + 7
        dic={}
        for i in s:
            dic[i]=0
        c=0
        old=0
        for i in s:
            old=c
            c=(2*c+1-dic[i])%mod
            dic[i]=old+1
        return c