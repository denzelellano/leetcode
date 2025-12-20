from collections import defaultdict

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by 
# using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.
 
# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterCountDict = defaultdict(int)
        
        for letter in magazine:
            letterCountDict[letter] += 1
            
        for letter in ransomNote:
            letterCountDict[letter] -= 1
            
        for count in letterCountDict.values():
            if count < 0:
                return False
        
        return True
            