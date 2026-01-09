class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        best = 0

        for x in s:
            if (x-1) not in s:
                cur = x
                l = 1

                while (cur + 1) in s:
                    cur += 1
                    l += 1

                best = max(best, l)

        return best

            
        


        