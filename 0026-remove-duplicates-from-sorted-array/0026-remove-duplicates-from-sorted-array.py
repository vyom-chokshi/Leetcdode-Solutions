class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num = []

        for i in nums:
            if i not in num:
                num.append(i)

        for i in range(len(num)):
            nums[i] = num[i]

        return len(num)