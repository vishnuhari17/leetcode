class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=range(0,len(nums)+1)
        for i in nums:
            if i in x:
                x.remove(i)
        for i in x:
            return i