class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        blank = []
        for i in nums:
            blank.append(i)

        for x in nums:
            blank.append(x)

        return blank