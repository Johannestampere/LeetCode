from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        sum = 0
        res = 0

        h = defaultdict(int) # cumulative sum: number of times we've seen that sum
        h[0] = 1

        for i in range(len(nums)): # at each pos, we ask if we've seen a running total = sum - k before
                                    # if yes, everything between that position and now must be equal to k
            sum += nums[i]

            if (sum - k) in h:
                res += h[sum-k]

            h[sum] += 1

        return res