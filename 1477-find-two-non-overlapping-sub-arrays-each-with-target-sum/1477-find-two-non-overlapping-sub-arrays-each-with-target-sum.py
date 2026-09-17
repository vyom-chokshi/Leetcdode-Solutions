class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
       
        n = len(arr)

        # best[i] = shortest target-sum subarray
        # completely within arr[0...i]
        best = [float('inf')] * n

        left = 0
        sm = 0
        ans = float('inf')
        best_len = float('inf')

        for right in range(n):

            sm += arr[right]

            while sm > target:
                sm -= arr[left]
                left += 1

            if sm == target:
                length = right - left + 1

            
                if left > 0 and best[left - 1] != float('inf'):
                    ans = min(ans, length + best[left - 1])

                best_len = min(best_len, length)

            best[right] = best_len

        return -1 if ans == float('inf') else ans