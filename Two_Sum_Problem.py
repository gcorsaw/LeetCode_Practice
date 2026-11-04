class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        integer_map = {}

        if len(nums) < 2:
            return []
        
        for index in range(len(nums)):
            number = nums[index]
            number_complement = target - number

            if number_complement in integer_map:
                return [integer_map[number_complement], index]

            integer_map[number] = index
        
        return[]