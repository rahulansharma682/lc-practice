class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        hM_s1 = {}
        s1Len = len(s1)

        for c in s1:
            if c in hM_s1:
                hM_s1[c] += 1
            else:
                hM_s1[c] = 1
        
        for i in range(len(s2) - s1Len + 1):
            comp = s2[i:i+s1Len]
            hM_s2 = {}

            for c in comp:
                if c in hM_s2:
                    hM_s2[c] += 1
                else:
                    hM_s2[c] = 1
                    
            if hM_s1 == hM_s2:
                return True
        
        return False

        
        

        
        