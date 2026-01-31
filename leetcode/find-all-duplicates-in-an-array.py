class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 3 3 2 2

        res = []
        
        for i in range(len(nums)):

            n = abs(nums[i])
            
            if nums[n-1] < 0:
                res.append(n)

            nums[n-1] = -nums[n-1]

        return res