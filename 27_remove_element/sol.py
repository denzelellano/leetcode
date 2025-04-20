from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] == val:
                k += 1
                if nums[r] == val:
                    r -= 1
                else:
                    nums[l] = nums[r]
                    nums[r] = val
                    l += 1
            else:
                l += 1

        print(nums)
                
        return k