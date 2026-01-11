class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hM = {}
        for n in nums:
            if n in hM:
                hM[n] += 2
            else:
                hM[n] = 1
        for k,v in hM.items():
            if v == 1:
                return k
        