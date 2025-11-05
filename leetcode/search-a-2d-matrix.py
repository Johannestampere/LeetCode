class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int top = 0;
        int bottom = matrix.size() - 1;

        while (top <= bottom) {
            int mid = (top + bottom) / 2;

            if (matrix[mid][0] < target) {
                top = mid + 1;
                continue;
            }

            else if (matrix[mid][0] > target) {
                bottom = mid - 1;
                continue;
            }

            else {
                return true;
            }
        }

        if (bottom < 0) return false;
        int row = bottom;

        int L = 0;
        int R = matrix[0].size() - 1;


        while (L <= R) {
            int mid = (L + R) / 2;

            if (matrix[row][mid] < target) {
                L = mid + 1;
                continue;
            }

            else if (matrix[row][mid] > target) {
                R = mid - 1;
                continue;
            }

            else {
                return true;
            }
        }

        return false;

    }
};