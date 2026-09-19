class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x=max(min(xCenter,x2),x1)
        y=max(min(yCenter,y2),y1)

        dx=x-xCenter
        dy=y-yCenter

        return (dx**2+dy**2<=radius**2)