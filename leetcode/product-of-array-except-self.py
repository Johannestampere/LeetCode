class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        left_multiplier = 1
        right_multiplier = 1
        n = len(nums)
        left_arr = [0] * n
        right_arr = [0] * n

        for i in range(n):
            j = -i - 1
            left_arr[i] = left_multiplier
            right_arr[j] = right_multiplier

            left_multiplier *= nums[i]
            right_multiplier *= nums[j]

        return [l*r for l, r in zip(left_arr, right_arr)]