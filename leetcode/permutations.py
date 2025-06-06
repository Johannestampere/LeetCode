class Solution(object):
    def permute(self, nums):
        # n! * (n^2)
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:]) # take the first num from nums out and add it to every index in every possible permutation of all the others 
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                cpy = list(p)
                cpy.insert(i, nums[0])
                res.append(cpy)

        return res