class Solution(object):
    def findMin(self, nums):
        L, R = 0, len(nums)-1
        res = nums[0]

        while L <= R:

            if nums[L] < nums[R]:    
                res = min(res, nums[L])  
                break      
                
            mid = (R + L) // 2

            res = min(res, nums[mid])

            if nums[mid] >= nums[L]:
                L = mid + 1
            else:
                R = mid - 1
            
        return res