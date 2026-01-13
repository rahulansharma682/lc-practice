class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        sLen = len(s)
        for i in range(sLen//2):
            s[i], s[sLen - i - 1] = s[sLen - i - 1], s[i]
             
        