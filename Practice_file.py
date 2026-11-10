class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        counted_s = {}
        counted_t = {}

        for i in range(len(s)):
            counted_s[s[i]] = 1 + counted_s.get(s[i], 0)
            counted_t[t[i]] = 1 + counted_t.get(t[i], 0)
        
        return counted_s == counted_t