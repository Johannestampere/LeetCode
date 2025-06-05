# Sliding window
# TC: O(n)
# SC: O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        maxlen = 0
        sub = set()

        for r in range(len(s)):
             
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            
            curwindowlen = r - l + 1
            sub.add(s[r])
            maxlen = max(maxlen, curwindowlen)
        
        return maxlen