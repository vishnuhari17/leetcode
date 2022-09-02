class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)

        # Or Approach given below can be used

        """
        i = nums.count(val)
        for r in range(0, i ):
            nums.remove(val)
        """