class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        list1=[]
        count=0
        for i in jewels:
            if i not in list1:
                list1.append(i)
        for i in stones:
            if i in list1:
                count+=1
        return count