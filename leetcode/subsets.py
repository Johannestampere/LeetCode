class Solution(object):
    def subsets(self, nums):
        
        res, subset = [], []

        def dfs(i):
            if i == len(nums): # base case: we're at the leaf node
                res.append(list(subset))
                return
            
            # choose to pick nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # choose not to pick nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res