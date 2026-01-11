class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        s = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in s:
                res.append(i)
        return res
        