class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        map_of_integers = {}

        if len(nums) < 2:
            return []

        for index in range(len(nums)):
            num = nums[index]
            numbers_complement = target - num

            if numbers_complement in map_of_integers:
                return [map_of_integers[numbers_complement], index]
            map_of_integers[num] = index

        return []