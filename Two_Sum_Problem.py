class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_num_map ={}
        for index, num in enumerate (nums):
            complement = target - num
            if complement in index_num_map:
                return [index_num_map[complement], index]
            index_num_map[num] = index
        return []