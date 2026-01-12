class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        n = len(nums)
        dq = deque()

        for r in range(n):
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()
            dq.append(r)

            if dq[0] <= r - k:
                dq.popleft()
            
            if r >= k - 1:
                res.append(nums[dq[0]])
        
        return res
        
        