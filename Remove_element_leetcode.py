class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # This approach can be used

        while val in nums:
            nums.remove(val)

        # Or Approach given below can be used(Both have similar run time)

        """
        i = nums.count(val)
        for r in range(0, i ):
            nums.remove(val)
        """