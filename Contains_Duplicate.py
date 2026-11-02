class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_of_nums = set(nums)
        if len(set_of_nums) < len(nums):
            return True
        else:
            return False