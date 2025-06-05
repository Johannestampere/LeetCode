# O(n) solution, prolly better one available

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsofar = 0
        max_at_i = 0

        # the logic is that if all the nums are negative, then just return the biggest number
        negative_check = True

        for i in range(len(nums)):
            if nums[i] >= 0:
                negative_check = False
            max_at_i = max(max_at_i + nums[i], 0) #reset if sum at position i becomes negative
            if maxsofar < max_at_i:
                maxsofar = max_at_i

        if negative_check:
            return max(nums)
        
        return maxsofar