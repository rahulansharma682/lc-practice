class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hM = {}
        for n in nums:
            hM[n] = hM.get(n, 0) + 1
        for k,v in hM.items():
            if v > len(nums)//2:
                return k
        