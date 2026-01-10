class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lowerString = []
        for ch in s:
            if ch.isalnum():
                lowerString.append(ch.lower())

        l = len(lowerString)
        for i in range(l // 2):
            if lowerString[i] != lowerString[l-1-i]:
                return False
                
        return True
        