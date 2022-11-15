class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        list = []
        for i in nums1:
            if i in nums2:
                if i not in list:
                    list.append(i)
                nums2.remove(i)
        return list

