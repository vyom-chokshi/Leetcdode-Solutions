class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        graph = {}

        for row, seat in reservedSeats:
            graph.setdefault(row, set()).add(seat)

        ans = (n - len(graph)) * 2

        for row in graph:
            seats = graph[row]

            left = not any(s in seats for s in [2, 3, 4, 5])
            middle = not any(s in seats for s in [4, 5, 6, 7])
            right = not any(s in seats for s in [6, 7, 8, 9])

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans