class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i1 = 0
        i2 = len(numbers) - 1
        while i1 < i2:
            s = numbers[i1] + numbers[i2]
            if s == target:
                return [i1 + 1, i2 + 1]
            elif s < target:
                i1 += 1
            else:
                i2 -= 1
        return []