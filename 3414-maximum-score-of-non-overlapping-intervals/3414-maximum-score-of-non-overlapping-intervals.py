from bisect import bisect_right
from functools import lru_cache


class Solution:
    def maximumWeight(self, intervals):
        # [left, right, weight, original_index]
        arr = [
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        ]

        # Sort by left endpoint
        arr.sort()

        n = len(arr)

        # Only left endpoints are needed for binary search
        starts = [x[0] for x in arr]

        @lru_cache(None)
        def dp(i, k):
            # No intervals left or cannot select anymore
            if i == n or k == 0:
                return (0, ())

            # -----------------
            # 1. Don't take i
            # -----------------
            skip = dp(i + 1, k)

            # -----------------
            # 2. Take i
            # -----------------
            l, r, w, idx = arr[i]

            # First interval whose start > r
            j = bisect_right(starts, r)

            next_weight, next_indices = dp(j, k - 1)

            take_weight = w + next_weight

            # Keep indices sorted because the answer must
            # be lexicographically compared by original indices
            take_indices = tuple(sorted((idx,) + next_indices))

            take = (take_weight, take_indices)

            # -----------------
            # Compare
            # -----------------
            if take[0] > skip[0]:
                return take

            if take[0] < skip[0]:
                return skip

            # Same weight:
            # lexicographically smaller index list wins
            return min(take, skip)

        return list(dp(0, 4)[1])