class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)

        finalset = []

        for l in range(len(nums)):

            num1 = nums[l]
            
            # if this number is the same as the next one, skip
            if l > 0 and nums[l] == nums[l-1]:
                continue
            
            lo = l + 1
            hi = len(nums) - 1

            while lo < hi:
                cursum = num1 + nums[lo] + nums[hi]
                if cursum == 0:
                    finalset.append([num1, nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1

                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1
                elif cursum < 0:
                    lo += 1
                else:
                    hi -= 1
            
        return finalset