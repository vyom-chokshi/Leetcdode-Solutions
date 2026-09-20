class Solution:
    def reverseDegree(self, s: str) -> int:

        dic={}

        for i, ch in enumerate(string.ascii_lowercase):
            dic[ch] = 26 - i

        sm=0

        for i in range(len(s)):
            sm+=(i+1)*dic[s[i]]
            
        return sm