class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] += 1
        if digits[-1] == 9 and len(digits) == 1:
            digits[-1] = 1
            digits.append(0)
        else:
            x =-1
            while x > -len(digits) and x !=9:
                digits[x] = 0
                digits[x-1] += 1
                x -=1
        return digits