class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)

        if x == x[::-1]:
            return True
        else:
            return False
'''
        x = str(x)
        after = []

        for i in x:
            after.append(i)

        after.reverse()

        if x == ''.join(after):
            return True
        else:
            return False
'''