class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def solve(left, right):
            if left == right:
                return piles[left]

            if (left, right) in dp:
                return dp[(left, right)]

            take_left = piles[left] - solve(left + 1, right)
            take_right = piles[right] - solve(left, right - 1)

            dp[(left, right)] = max(take_left, take_right)
            return dp[(left, right)]

        return solve(0, len(piles) - 1) > 0