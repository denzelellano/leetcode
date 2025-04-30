'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,1,3,1,2]
Output: 2


'''

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numDict: dict[int, int] = {}
        for num in nums:
            if num not in numDict:
                numDict[num] = 1
            else:
                numDict[num] += 1
        
        middle = len(nums) // 2
        for num in numDict:
            if numDict[num] > middle:
                return num