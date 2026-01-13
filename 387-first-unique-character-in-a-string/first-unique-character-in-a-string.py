class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hM = {}
        for c in s:
            hM[c] = hM.get(c, 0) + 1
        for i in range(len(s)):
            if hM[s[i]] == 1:
                return i
        return -1
        