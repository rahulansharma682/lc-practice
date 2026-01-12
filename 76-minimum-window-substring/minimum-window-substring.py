class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tLen = len(t)
        sLen = len(s)

        if tLen > sLen:
            return ""

        thM = {}
        for c in t:
            thM[c] = thM.get(c, 0) + 1
        
        window = {}
        requiredChars = len(thM)
        formed = 0

        bestLen = float('inf')
        bestL = 0
        bestR = 0
        
        l = 0
        for r in range(sLen):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in thM and window[c] == thM[c]:
                formed += 1

            while formed == requiredChars:
                if r - l + 1 < bestLen:
                    bestLen = r - l + 1
                    bestL, bestR = l, r

                leftChar = s[l]
                window[leftChar] -= 1

                if leftChar in thM and window[leftChar] < thM[leftChar]:
                    formed -= 1
                if  window[leftChar] == 0:
                    del window[leftChar]
                l += 1
        
        if bestLen == float('inf'):
            return ""
        else:
            return s[bestL: bestR + 1]        