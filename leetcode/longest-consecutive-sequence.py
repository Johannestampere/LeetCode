class Solution(object):
    def longestConsecutive(self, nums):
        s = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in s:
                curLen = 0
                while (n + curLen) in s:
                    curLen += 1
                longest = max(longest, curLen)
            
        return longest