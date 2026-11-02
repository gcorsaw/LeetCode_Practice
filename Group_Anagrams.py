class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group_anagrams = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in group_anagrams:
                group_anagrams[sorted_string].append(string)
            else:
                group_anagrams[sorted_string] = [string]
        return list(group_anagrams.values())