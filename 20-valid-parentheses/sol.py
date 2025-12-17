# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Example 5:
# Input: s = "([)]"
# Output: false

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        openBracketStack = []
        
        for bracket in s:
            currBracketStack = openBracketStack[-1] if openBracketStack else ''
            if bracket == '(' or bracket == '[' or bracket == '{':
                openBracketStack.append(bracket)
            elif (bracket == ')' and currBracketStack == '(') or (bracket == ']' and currBracketStack == '[') or (bracket == '}' and currBracketStack == '{'):
                openBracketStack.pop()
            else:
                return False
                
        if openBracketStack:
            return False
        
        return True
    
    
sol = Solution()

print(sol.isValid('()[]{}'))