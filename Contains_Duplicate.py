class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        set_of_numbers = set()

        for value in nums:
            if value in set_of_numbers:
                return True
            set_of_numbers.add(value)
        return False