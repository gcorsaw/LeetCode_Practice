class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_index_map ={}
        if len(nums) < 2:
            return []
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_index_map:
                return [num_index_map[complement], index]
            num_index_map[num] = index
        return []