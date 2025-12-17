from collections import defaultdict

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letterDict = defaultdict(int)
        
        for letter in s:
            letterDict[letter] +=1
        
        for letter in t:
            letterDict[letter] -= 1
            
        for count in letterDict.values():
            if count != 0:
                return False
            
        return True
    
sol = Solution()
res = sol.isAnagram("anagram", "nagaram")
print(res)