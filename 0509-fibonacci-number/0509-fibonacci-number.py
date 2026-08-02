class Solution:
    def fib(self, n: int) -> int:
        dic={}
        def solve(n):
            if n==0:
                return 0
            if n==1:
                return 1
            if n in dic:
                return dic[n]
            dic[n]=self.fib(n-1)+self.fib(n-2)
            return dic[n]
        return solve(n)