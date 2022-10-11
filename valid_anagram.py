class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        list1 = []
        list2 = []
        for i in s:
            list1.append(i)
        for i in t:
            list2.append(i)
        list1 = list1.sort()
        list2 = list2.sort()
        if list1 == list2:
            return True
        else:
            return False