class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split(" ") # arr of words
        if len(s) != len(pattern): 
            return False

        L_to_W, W_to_L = {}, {}

        for i in range(len(s)):
            if (pattern[i] in L_to_W and L_to_W[pattern[i]] != s[i]) or (s[i] in W_to_L and W_to_L[s[i]] != pattern[i]):
                return False
            L_to_W[pattern[i]] = s[i]
            W_to_L[s[i]] = pattern[i]

        return True