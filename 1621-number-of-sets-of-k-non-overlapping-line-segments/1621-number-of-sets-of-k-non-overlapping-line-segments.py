class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        m=(10**9+7)
        if (n+k-1)<2*k:
            return 0
        return math.comb(n+k-1,2*k)%m