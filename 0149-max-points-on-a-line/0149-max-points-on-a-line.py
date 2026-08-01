from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = {}
            curr_max = 0

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

            
                g = gcd(dx, dy)
                dx //= g
                dy //= g

                
                if dx < 0:
                    dx *= -1
                    dy *= -1
                elif dx == 0:
                    dy = 1          
                elif dy == 0:
                    dx = 1          

                slope = (dy, dx)

                if slope in slopes:
                    slopes[slope] += 1
                else:
                    slopes[slope] = 1

                curr_max = max(curr_max, slopes[slope])

            ans = max(ans, curr_max + 1)

        return ans