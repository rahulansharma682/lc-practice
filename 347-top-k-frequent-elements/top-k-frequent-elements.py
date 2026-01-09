class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hM = {}
        for n in nums:
            if n in hM:
                hM[n] += 1
            else:
                hM[n] = 1
        
        sorted_hM = sorted(hM.items(), key = lambda x: x[1], reverse = True)
        ans = []
        for k,v in sorted_hM[:k]:
            ans.append(k)
        return ans


        