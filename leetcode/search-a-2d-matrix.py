# First do binary search on the rows themselves
# then do binary search in the correct row

class Solution(object):
    def searchMatrix(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1

        while top <= bot:
            row = bot + (top - bot) // 2

            if target > matrix[row][-1]:
                top = row + 1
            
            elif target < matrix[row][0]:
                bot = row - 1
            
            else:
                break
            
        if not (top <= bot):
            return False
        
        row = (top + bot) // 2
    
        l, r = 0, cols - 1

        while l <= r:

            mid = l + (r - l) // 2

            if target > matrix[row][mid]:
                l = mid + 1
            
            elif target < matrix[row][mid]:
                r = mid - 1
            
            else:
                return True
            
        return False