class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        length = len(palindrome)
        if length != 1:
            count = palindrome.count("a")
            if count == length:
                palindrome = palindrome[::-1]
                palindrome = palindrome.replace("a", "b", 1)
                palindrome = palindrome[::-1]
                return palindrome
            else:
                if palindrome.count("a") + 1 == length:
                    palindrome = palindrome[::-1]
                    palindrome = palindrome.replace("a", "b", 1)
                    palindrome = palindrome[::-1]
                    print(1)
                    return palindrome

                else:
                    for i in range(0, length):
                        if palindrome[i] != "a":
                            palindrome = palindrome.replace(palindrome[i], "a", 1)
                            return palindrome
        else:
            return ""

        return palindrome