class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        number_set = set()
        for num_value in nums:
            if num_value in number_set:
                return True
            number_set.add(num_value)
        return False