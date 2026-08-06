class Solution(object):
    def smallestNumber(self, n, t):

        def pro(x):
            p = 1
            while x > 0:
                p *= x % 10
                x //= 10
            return p

        while pro(n) % t != 0:
            n += 1

        return n