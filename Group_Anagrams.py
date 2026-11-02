class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram = {}
        for words in strs:
            sorted_word = ''.join(sorted(words))
            if sorted_word not in anagram:
                anagram[sorted_word] = [words]
            else:
                anagram[sorted_word].append(words)
        return anagram.values()