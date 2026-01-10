class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        maxArea = 0

        while l < r:
            s1 = min(height[l], height[r])
            s2 = r - l 
            areaWater = s1*s2
            if areaWater > maxArea:
                maxArea = areaWater
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea



        