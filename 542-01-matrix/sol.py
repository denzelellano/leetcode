# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]

from cmath import inf
from typing import List


class Solution:
    
    def getZerosQueue(self, mat) -> List[List[int]]:
        q = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    q.append((row, col))
                else:
                    mat[row][col] = inf
                    
        return q
            
        
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = self.getZerosQueue(mat)
        for qRow, qCol in q:
            for (row, col) in (1, 0), (-1, 0), (0, 1), (0, -1):
                (nRow, nCol) = (row + qRow, col + qCol)
                if nRow < 0 or nRow >= len(mat) or nCol < 0 or nCol >= len(mat[0]) or mat[nRow][nCol] != inf:
                    continue
                
                mat[nRow][nCol] = 1 + mat[qRow][qCol]
                q.append((nRow, nCol))
            
            
        return mat
    
test = Solution()

mat = [[0,0,0],[0,1,0],[0,0,0]]
res = test.updateMatrix(mat)

print(res)