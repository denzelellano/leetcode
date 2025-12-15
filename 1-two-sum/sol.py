from typing import List

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        
        for i, num in enumerate(nums):
            if target - num in numDict:
                return [numDict[target - num], i]
            else:
                numDict[num] = i
                
        return []
    
sol = Solution()

nums = [2,7,11,15]
target = 9


print(sol.twoSum(nums, target))