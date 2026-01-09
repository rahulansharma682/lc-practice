class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hM = {}
        for i in range(len(nums)):
            hM[nums[i]] = i

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hM and hM[comp] != i:
                return [i, hM[comp]]
        return [] 
        