# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 
# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        carry = 0
        
        a = a[::-1]
        b = b[::-1]
        
        for i in range(max(len(a), len(b))):
            numA: int = ord(a[i]) - ord('0') if i < len(a) else 0
            numB: int = ord(b[i]) - ord('0') if i < len(b) else 0
            
            sum = numA + numB + carry
            
            if sum == 3:
                carry = 1
                res = '1' + res
            elif sum == 2:
                carry = 1
                res = '0' + res
            elif sum == 1:
                carry = 0
                res = '1' + res
            else:
                carry = 0
                res = '0' + res
                
        return '1' + res if carry else res
        
sol = Solution()
res = sol.addBinary('11', '1')
print(res)