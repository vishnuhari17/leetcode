class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_count=0
        count=0
        for i in sentences:
            j=i.split()
            count=len(j)
            if count>max_count:
                    max_count=count
        return max_count