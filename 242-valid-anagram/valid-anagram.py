class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
            
        hS = {}
        for letter in s:
            if letter in hS:
                hS[letter] += 1
            else:
                hS[letter] = 1
        
        hT = {}
        for letter in t:
            if letter in hT:
                hT[letter] += 1
            else:
                hT[letter] = 1
        
        for k,v in hS.items():
            if k not in hT or hT[k] != v:
                return False

        return True
        
        