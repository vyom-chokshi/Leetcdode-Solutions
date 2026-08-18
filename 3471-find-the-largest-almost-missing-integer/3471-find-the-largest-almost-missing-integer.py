class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        dic = {}

        for i in range(len(nums) - k + 1):
            seen = set()

            for j in range(i, i + k):
                seen.add(nums[j])

            for x in seen:
                dic[x] = dic.get(x, 0) + 1

        ans = -1

        for x in dic:
            if dic[x] == 1:
                ans = max(ans, x)

        return ans