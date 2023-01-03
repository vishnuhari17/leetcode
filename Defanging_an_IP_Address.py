class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        str2=""
        for i in address:
            if i==".":
                str2=str2+"[.]"
            else:
                str2=str2+i
        return str2