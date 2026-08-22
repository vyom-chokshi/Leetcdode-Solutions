class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x = 0
        y = 1
        l = n

        while l > 0:
            digit = l % 10
            x += digit
            y *= digit
            l //= 10

        return n % (y+x) == 0
