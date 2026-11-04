class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set()
        
        for values in nums:
            if values in num_set:
                return True
            num_set.add(values)
        
        return False