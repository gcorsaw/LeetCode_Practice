class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        int_count = {}
        for num in nums:
            int_count[num] = int_count.get(num, 0) + 1
        sorted_int_count = sorted(int_count.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_int_count[:k]]