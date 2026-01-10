class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p = 0
        for n in nums:
            if n == val:
                continue
            else:
                nums[p] = n
                p += 1
        return p
        

        