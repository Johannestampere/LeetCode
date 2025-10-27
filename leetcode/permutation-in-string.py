from collections import defaultdict

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) > len(s2):
            return False
        
        h1 = defaultdict(int)
        h2 = defaultdict(int)

        for l in s1:
            h1[l] += 1

        window_size = len(s1)

        # build the initial map for s2 counts
        for i in range(window_size):
            h2[s2[i]] += 1
        
        if h1 == h2:
            return True

        # slide window
        for i in range(window_size, len(s2)):
            h2[s2[i]] += 1
            h2[s2[i - window_size]] -= 1

            if h2[s2[i - window_size]] == 0:
                del h2[s2[i - window_size]]
            
            if h1 == h2:
                return True

        return False