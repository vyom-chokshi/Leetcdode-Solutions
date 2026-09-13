class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        dic={}
        for i, x in enumerate(nums):
            if x not in dic:
                dic[x] = []
            dic[x].append(i)
        count = 0

        for num, indexes in dic.items():
            if len(indexes) < 3:
                continue

            distance = indexes[1] - indexes[0]

            for i in range(2, len(indexes)):
                if indexes[i] - indexes[i-1] != distance:
                    break
            else:
                count += 1
        return count