# recursive backtracking:
# the L path says let's keep using the num at index i
# the R path says let's not ever use that number again

class Solution(object):
    def combinationSum(self, candidates, target):
        
        res, sol = [], []

        n = len(candidates)

        def backtrack(i, curSum):
            if curSum == target:
                res.append(sol[:])
                return
            
            if curSum > target or i == n:
                return

            # right path, let's use no more of the num at index i
            # cursum doesnt change because we didnt decide to use that num
            backtrack(i + 1, curSum)

            # left path, let's use that num
            sol.append(candidates[i])
            backtrack(i, curSum + candidates[i])
            
            # undo using that number
            sol.pop()

        backtrack(0, 0)

        return res