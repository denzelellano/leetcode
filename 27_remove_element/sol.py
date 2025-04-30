from typing import List

class Solution:
    
    # With for loop
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1

        return l
    
    # With while loop:
    # def removeElement(self, nums: List[int], val: int) -> int:
    # l = 0
    # r = len(nums) - 1
    
    # while l <= r:
    #     if nums[l] == val:
    #             nums[l] = nums[r]
    #             r -=1
    #     else:
    #         l += 1
    # return l