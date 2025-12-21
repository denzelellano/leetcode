# Given a string s which consists of lowercase or uppercase letters, 
# return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        oddLetterCountSet = set()
        
        for letter in s:
            if letter in oddLetterCountSet:
                oddLetterCountSet.remove(letter)
            else:
                oddLetterCountSet.add(letter)
                
        if not oddLetterCountSet:
            return len(s)
        
        return len(s) - len(oddLetterCountSet) + 1