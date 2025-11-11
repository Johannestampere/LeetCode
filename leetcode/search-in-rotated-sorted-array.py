class Solution {
public:
    int search(vector<int>& nums, int target) {
        int L = 0;
        int R = nums.size() - 1;

        while (L < R) {
            int M = (R + L) / 2;

            if (nums[M] > nums[R]) {
                L = M + 1;
            }

            else {
                R = M;
            }
        }

        int min_index = L;

        if (min_index == 0) {
            L = 0;
            R = nums.size() - 1;
        }
        else if (target >= nums[0] && target <= nums[min_index-1]) {
            L = 0;
            R = min_index - 1;
        }
        else {
            L = min_index;
            R = nums.size()-1;
        }

        while (L <= R) {
            int M = (L + R) / 2;

            if (target > nums[M]) {
                L = M + 1;
            }
            else if (target < nums[M]) {
                R = M - 1;
            }
            else {
                return M;
            }
        }

        return -1;
    }
};