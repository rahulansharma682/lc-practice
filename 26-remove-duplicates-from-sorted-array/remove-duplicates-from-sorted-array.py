class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        i = 0
        for n in nums:
            if n not in s:
                nums[i] = n
                s.add(n)
                i += 1   
        return i
        