class Solution(object):
    def maxArea(self, height):
        n = len(height)
        l, r = 0, n-1

        maxArea = 0

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            a = w * h
            maxArea = max(maxArea, a)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea