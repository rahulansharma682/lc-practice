class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        hM_s1 = {}
        hM_s2 = {}
        s1Len = len(s1)
        s2Len = len(s2)

        if s1Len > s2Len:
            return False

        for c in s1:
            if c in hM_s1:
                hM_s1[c] += 1
            else:
                hM_s1[c] = 1
        
        for i in range(s1Len):
            c = s2[i]
            if c in hM_s2:
                hM_s2[c] += 1
            else:
                hM_s2[c] = 1
        
        if hM_s1 == hM_s2:
            return True
        
        for r in range(s1Len, s2Len):
            newChar = s2[r]

            if newChar in hM_s2:
                hM_s2[newChar] += 1
            else:
                hM_s2[newChar] = 1
            
            removeOldChar = s2[r - s1Len]
            hM_s2[removeOldChar] -= 1

            if hM_s2[removeOldChar] == 0:
                del hM_s2[removeOldChar]
            
            if hM_s1 == hM_s2:
                return True

        return False