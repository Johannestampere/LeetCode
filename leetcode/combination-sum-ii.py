class Solution(object):
    def combinationSum2(self, candidates, target):
        nums = candidates
        n = len(nums)

        nums = sorted(nums)

        res = []

        def dfs(i, curComb, curTotal):
            if curTotal == target:
                res.append(list(curComb))
                return

            if curTotal > target or i >= n:
                return

            # include the element at index i
            curComb.append(nums[i])
            # pass the next index, new comb, and new total
            dfs(i + 1, curComb, curTotal + nums[i])
            # get curComb ready for the next dfs
            curComb.pop()

            # skip element at index i
            #   dont wanna use duplicate elements
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, curComb, curTotal)
            
        dfs(0, [], 0)
        return res