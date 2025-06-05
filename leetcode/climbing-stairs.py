class Solution(object):
    def climbStairs(self, n):

        if n == 1:
            return 1
        if n == 2:
            return 2

        prev = 1
        cur = 2

        for i in range(2, n):
            nextt = prev + cur
            prev = cur
            cur = nextt
        
        return cur