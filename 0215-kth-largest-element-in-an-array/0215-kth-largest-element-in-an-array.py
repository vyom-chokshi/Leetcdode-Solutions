class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num=sorted(nums)
        return num[len(num)-k]