from typing import Optional

# Ex: 1
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Ex: 2
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Ex: 3
# Input: root = []
# Output: true

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.calcHeight(root) >= 0
        
    def calcHeight(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        
        leftMax = self.calcHeight(node.left)
        rightMax = self.calcHeight(node.right)
        
        isNotHeightBalanced = abs(leftMax - rightMax) > 0 or leftMax < 0 or rightMax < 0
        if isNotHeightBalanced:
            return -1
        
        return abs(leftMax, rightMax) + 1