class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # in our cur window, whatever element is the most 
        #   frequent is the one we will try to convert the 
        #   others to

        maxSoFar = 0
        L = 0
        counts = [0] * 26 # array of counts for every letter in the alphabet

        for R in range(len(s)):
            counts[ord(s[R]) - 65] += 1 # ord(s[R]) is  a characters ascii number, A = 65

            # while the window is invalid
            while (R - L + 1) - max(counts) > k:
                counts[ord(s[L]) - 65] -= 1
                L += 1

            maxSoFar = max(maxSoFar, R - L + 1)
        
        return maxSoFar