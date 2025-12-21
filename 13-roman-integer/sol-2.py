# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 
# 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. 
# However, the numeral for four is not IIII. Instead, the number four is written as IV. 
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. 
# There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 
# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

from enum import Enum

class Solution:
    # class Numeral(Enum):
    #     I = 1
    #     V = 5
    #     X = 10
    #     L = 50
    #     C = 100
    #     D = 500
    #     M = 1000
        
    # def romanToInt(self, s: str) -> int:
    #     sum = 0
        
    #     for i, character in enumerate(s):
            
    #         prevNumeral = self.Numeral[s[i-1]] if i > 0 else None
            
    #         if character == self.Numeral.I.name:
    #             sum += self.Numeral.I.value
                
    #         if character == self.Numeral.V.name:
    #             sum += self.calculateAddition(self.Numeral.V, prevNumeral, self.Numeral.I)
                
    #         if character == self.Numeral.X.name:
    #             sum += self.calculateAddition(self.Numeral.X, prevNumeral, self.Numeral.I)
                
    #         if character == self.Numeral.L.name:
    #             sum += self.calculateAddition(self.Numeral.L, prevNumeral, self.Numeral.X)
                
    #         if character == self.Numeral.C.name:
    #             sum += self.calculateAddition(self.Numeral.C, prevNumeral, self.Numeral.X)
                
    #         if character == self.Numeral.D.name:
    #             sum += self.calculateAddition(self.Numeral.D, prevNumeral, self.Numeral.C)
                
    #         if character == self.Numeral.M.name:
    #             sum += self.calculateAddition(self.Numeral.M, prevNumeral, self.Numeral.C)
                
    #     return sum
                
    # def calculateAddition(self, numeralToAdd: Numeral, prevNumeral: Numeral, numeralToSubtract: Numeral):
    #     if prevNumeral == numeralToSubtract:
    #         return numeralToAdd.value - (numeralToSubtract.value * 2)
        
    #     return numeralToAdd.value
    
    def romanToInt(self, s: str) -> int:
        numeralsDict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        sum = 0
        for i in range(len(s)):
            if (i + 1) < len(s) and numeralsDict[s[i + 1]] > numeralsDict[s[i]]:
                sum -= numeralsDict[s[i]]
            else:
                sum += numeralsDict[s[i]]
                
        return sum