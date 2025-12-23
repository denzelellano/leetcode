# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 1st solution with sorting:
        # firstStr = min(strs)
        # lastStr = max(strs)
        # longestPrefix = ''
        
        # for i in range(min(len(firstStr), len(lastStr))):
        #     if firstStr[i] != lastStr[i]:
        #         return longestPrefix

        #     longestPrefix += firstStr[i]
            
        # return longestPrefix
        
        # 2nd solution using first word to compare against all other words
        if not strs:
            return ''
        
        currPrefix = strs[0]
        
        for word in strs[1:]:
            while not word.startswith(currPrefix):
                currPrefix = currPrefix[:-1]
                
                if not currPrefix:
                    return ''
                
        return currPrefix
    
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))