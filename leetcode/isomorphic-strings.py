class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ST_map, TS_map = {}, {}

        for i in range(len(s)):
            if (s[i] in ST_map and ST_map[s[i]] != t[i]) or (t[i] in TS_map and TS_map[t[i]] != s[i]):
                return False
            ST_map[s[i]] = t[i]
            TS_map[t[i]] = s[i]
        
        return True