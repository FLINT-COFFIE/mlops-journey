# Time complexity: O(nlog⁡n)
# Space complexity: O(n)
# ===========================

# Current
# Time complexity: O(n)
# Space complexity: O(n)

## reducing time complexity to O(n)
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if sorted(s) == sorted(t) and len(s) == len(t):
        if len(s) != len(t): 
            return False
        return Counter(s) == Counter(t)
    
  
    

