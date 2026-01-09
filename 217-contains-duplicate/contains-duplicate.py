class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hM = {}
        for n in nums:
            if n in hM:
                return True
            else:
                hM[n] = 1
        return False
        