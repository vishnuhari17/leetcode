class Solution(object):
    def twoSum(self, nums, target):
        #method of hashtable is used as runtime matters
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(0,len(nums)):
            if target - nums[i] in seen:
                return [i,seen[target - nums[i]]]
            else:
                seen[nums[i]] = i
