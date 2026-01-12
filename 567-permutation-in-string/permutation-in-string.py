class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        key = ''.join(sorted(s1))
        for i in range(len(s2) - len(key) + 1):
            r = s2[i:i+len(key)]
            if key == ''.join(sorted(r)):
                return True
        return False

        
        