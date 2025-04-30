from typing import List
from math import sqrt

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
# return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Ex: If k = 1 and we have 2 points given, we must return the point closest to (0, 0)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) < k:
            return None
        
        originX = originY = 0
        
        diffMap = {}
        
        for i in range(len(points)):
            # get dist from origin
            pointX = points[i][0]
            pointY = points[i][1]
            
            xDiff = abs(pointX - originX)
            xSqr = xDiff ** 2
            
            yDiff = abs(pointY - originY)
            ySqr = yDiff ** 2
            
            diffRes = sqrt(xSqr + ySqr)
            
            diffMap[i] = diffRes
            
        
        
            
        return resList
    
        
        
test = Solution()

sample1 = [[1, 1], [0, 1]]
print(test.kClosest(sample1, 1))