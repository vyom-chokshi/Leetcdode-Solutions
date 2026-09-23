class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:

        n = len(nums)
        target = sum(nums) - x

        if target < 0:
            return -1

        if target == 0:
            return n

        mp = {0: -1}

        prefix = 0
        max_len = -1

        for i in range(n):
            prefix += nums[i]

        
            if prefix - target in mp:
                length = i - mp[prefix - target]
                max_len = max(max_len, length)

            
            if prefix not in mp:
                mp[prefix] = i

        if max_len == -1:
            return -1

        return n - max_len
