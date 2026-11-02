class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        answer = [0]*length
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
            reverse_product = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * reverse_product
            reverse_product *= nums[i]
        return answer
            