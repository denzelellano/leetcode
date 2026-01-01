# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two cells sharing a common edge is 1.

# Example 1:
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]

# Example 2:
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
 
# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.

# Note: This question is the same as 1765: https://leetcode.com/problems/map-of-highest-peak/

from typing import List
from collections import deque
from cmath import inf

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = inf
    
        while queue:
            row, col = queue.popleft()
            
            for directionRow, directionCol in directions:
                currRow = row + directionRow
                currCol = col + directionCol
                
                isOutOfMatrixRange = currRow < 0 or currRow >= len(mat) or currCol < 0 or currCol >= len(mat[0])
                
                if isOutOfMatrixRange or mat[currRow][currCol] != inf:
                    continue
                
                mat[currRow][currCol] = 1 + mat[row][col]
                queue.append((currRow, currCol))
                
        return mat
    
    
test = Solution()

mat = [[0,0,0],[0,1,0],[1,1,1]]
res = test.updateMatrix(mat)

print(res)